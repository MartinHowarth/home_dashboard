# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import importlib
import json
import logging
import os
import sys

from dash.dependencies import Input, Output
from flask import Flask

from home_dashboard import bus, birthday, train, clock, weather
from home_dashboard.config_model import HomeDashboard

CSS_DICT = {
    'minty': 'https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/minty/bootstrap.min.css'
}


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

    return HomeDashboard(config_module.config)


def load_config_from_env() -> HomeDashboard:
    return HomeDashboard(json.loads(os.environ['ALL_CONFIG']))


def create_app_layout(_config: HomeDashboard):
    def regenerate_layout():
        return html.Div(
            children=[
                html.Div(id='update-clock'),
                html.Div(id='update-bus-train', className="row"),
                html.Div(id='update-birthdays'),
                html.Img(id='update-weather', style={'display': 'inline-block',
                                                     'width': '20%',
                                                     'vertical-align': 'middle'}),
                dcc.Interval(
                    id='fast-interval',
                    interval=500,  # in milliseconds
                    n_intervals=0
                ),
                dcc.Interval(
                    id='slow-interval',
                    interval=30 * 1000,  # in milliseconds
                ),
                dcc.Interval(
                    id='really-slow-interval',
                    interval=60 * 60 * 1000,  # in milliseconds
                ),
            ],
            className="container",
        )
    return regenerate_layout


def create_app_callbacks(_app, _config):
    @_app.callback(Output('update-bus-train', 'children'),
                   [Input('slow-interval', 'n_intervals')])
    def update_train_bus_row(n):
        return [
            bus.generate_bus_arrivals_div(_config.bus),
            train.generate_train_departures_div(_config.train),
        ]

    @_app.callback(Output('update-clock', 'children'),
                   [Input('fast-interval', 'n_intervals')])
    def update_clock(n):
        return [clock.generate_clock_div()]

    @_app.callback(Output('update-birthdays', 'children'),
                   [Input('really-slow-interval', 'n_intervals')])
    def update_birthdays(n):
        return [birthday.generate_upcoming_birthdays_div(_config.birthday)]

    @_app.callback(Output('update-weather', 'src'),
                   [Input('really-slow-interval', 'n_intervals')])
    def update_weather(n):
        return weather.get_weather_icon_url(_config.weather)

    _all_updates = [
        update_train_bus_row,
        update_clock,
        update_birthdays,
        update_weather,
    ]
    return _all_updates


try:
    config = load_config_from_env()
except KeyError:
    config = load_config_from_file()

bus.download_bus_stop_info()

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash(name=__name__, server=server)
app.layout = create_app_layout(config)

# Force all updates immediately so we don't have to wait for the timer(s) to pop.
all_updates = create_app_callbacks(app, config)
[update(0) for update in all_updates]

# Use Minty CSS
app.css.append_css({"external_url": CSS_DICT['minty']})

if __name__ == "__main__":
    configure_logging()
    app.run_server(threaded=True, port=int(os.environ.get('PORT', 80)), debug=True)
