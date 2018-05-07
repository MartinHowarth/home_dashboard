# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import importlib
import itertools
import json
import logging
import os
import sys

from dash.dependencies import Input, Output
from flask import Flask

from home_dashboard.config_model import HomeDashboard
from home_dashboard.constants import JAVASCRIPT_DIR, MAIN_JS_TEMPLATE
from home_dashboard.html_toolkit import layouts
from home_dashboard.widgets import weather, train, bus, birthday, wifi, visitor_book
from home_dashboard.widgets.base import render_javascript_template
from home_dashboard.widgets.clock import ClockWidget


log = logging.getLogger(__name__)


def configure_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def load_config_from_file() -> HomeDashboard:
    # Strip the .py extension
    config_file = os.path.splitext(sys.argv[1])[0]
    config_module = importlib.import_module(config_file)

    cfg = HomeDashboard(config_module.config, partial=False)
    cfg.validate()
    return cfg


def load_config_from_env() -> HomeDashboard:
    cfg = HomeDashboard(json.loads(os.environ['ALL_CONFIG']), partial=False)
    cfg.validate()
    return cfg


def create_app_layout(_config: HomeDashboard):
    clock_widget = ClockWidget(_config.clock)
    clock_widget.generate_javascript()

    js_loop_names = itertools.chain(
        clock_widget.js_initial_function_names
    )
    render_javascript_template(
        MAIN_JS_TEMPLATE,
        '',
        {
            'initial-functions': [
                {'function-name': fn_name}
                for fn_name in js_loop_names
            ]
        }
    )

    def regenerate_layout():
        return html.Div(
            children=[
                clock_widget.html_div,
                layouts.create_equal_row([
                    html.Div(id='update-bus'),
                    html.Div(id='update-train'),
                ]),
                html.Div(id='update-visitor-book', className="container"),
                layouts.create_equal_row([
                    html.Div(id='update-birthdays'),
                    layouts.create_equal_row([
                        html.Div(id='update-weather'),
                        wifi.generate_wifi_div(_config.wifi),
                    ]),
                ]),
                dcc.Interval(
                    id='30sec-interval',
                    interval=30 * 1000,  # in milliseconds
                ),
                dcc.Interval(
                    id='5minute-interval',
                    interval=5 * 60 * 1000,  # in milliseconds
                ),
                dcc.Interval(
                    id='1hour-interval',
                    interval=60 * 60 * 1000,  # in milliseconds
                ),
            ],
            className="container",
            id="main",  # Must match the ID in the "startLoops" javascript function.
        )
    return regenerate_layout


def create_app_callbacks(_app, _config):
    @_app.callback(Output('update-bus', 'children'),
                   [Input('30sec-interval', 'n_intervals')])
    def update_bus_row(n):
        return [bus.generate_bus_arrivals_div(_config.bus)]

    @_app.callback(Output('update-train', 'children'),
                   [Input('30sec-interval', 'n_intervals')])
    def update_train_row(n):
        return [train.generate_train_departures_div(_config.train)]

    @_app.callback(Output('update-visitor-book', 'children'),
                   [Input('5minute-interval', 'n_intervals')])
    def update_visitor_book(n):
        return [visitor_book.VisitorBookWidget(_config.visitor_book).html_div]

    @_app.callback(Output('update-birthdays', 'children'),
                   [Input('1hour-interval', 'n_intervals')])
    def update_birthdays(n):
        return [birthday.generate_upcoming_birthdays_div(_config.birthday)]

    @_app.callback(Output('update-weather', 'children'),
                   [Input('1hour-interval', 'n_intervals')])
    def update_weather(n):
        return [weather.generate_weather_div(_config.weather)]

    _all_updates = [
        update_birthdays,
        update_bus_row,
        update_train_row,
        update_visitor_book,
        update_weather,
    ]
    return _all_updates


try:
    config = load_config_from_env()
except KeyError:
    config = load_config_from_file()

bus.download_bus_stop_info()
wifi.generate_wifi_qr_code(config.wifi)

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash(name=__name__, server=server)
app.layout = create_app_layout(config)

# Force all updates immediately so we don't have to wait for the timer(s) to pop.
all_updates = create_app_callbacks(app, config)
try:
    # This can fail due to various API errors. During callbacks this is handled nicely,
    # but on initial start we have to catch it ourselves.
    [update(0) for update in all_updates]
except Exception as err:
    log.exception("Exception on initial updates: {}".format(err))

app.css.append_css({"external_url": config.css_cdn})

# Add each script to the app from the JAVASCRIPT_DIR
for script in os.listdir(JAVASCRIPT_DIR):
    if os.path.splitext(script)[1] != '.js':
        continue
    app.scripts.append_script({
        'external_url': '/static/{}'.format(script)
    })


# Use Flask to serve the javascript source files statically.
@app.server.route('/static/<filename>.js')
def serve_script(filename):
    return flask.send_from_directory(JAVASCRIPT_DIR, '{}.js'.format(filename))


if __name__ == "__main__":
    configure_logging()
    app.run_server(threaded=True, port=int(os.environ.get('PORT', 80)), debug=True)
