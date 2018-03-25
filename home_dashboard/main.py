# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import importlib
import json
import os
import sys

from dash.dependencies import Input, Output

from home_dashboard import bus, birthday, train, clock
from home_dashboard.config_model import HomeDashboard

CSS_DICT = {
    'minty': 'https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/minty/bootstrap.min.css'
}


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
                dcc.Interval(
                    id='fast-interval',
                    interval=500,  # in milliseconds
                    n_intervals=0
                ),
                dcc.Interval(
                    id='slow-interval',
                    interval=30 * 1000,  # in milliseconds
                    n_intervals=0
                ),
            ],
            className="container",
        )
    return regenerate_layout


def create_app_callbacks(app, _config):
    @app.callback(Output('update-bus-train', 'children'),
                  [Input('slow-interval', 'n_intervals')])
    def update_train_bus_row(n):
        return [
            bus.generate_bus_arrivals_div(_config.bus),
            train.generate_train_departures_div(_config.train),
        ]

    @app.callback(Output('update-clock', 'children'),
                  [Input('fast-interval', 'n_intervals')])
    def update_clock(n):
        return [clock.generate_clock_div()]

    @app.callback(Output('update-birthdays', 'children'),
                  [Input('slow-interval', 'n_intervals')])
    def update_birthdays(n):
        return [birthday.generate_upcoming_birthdays_div(_config.birthdays)]


def main():
    try:
        config = load_config_from_env()
    except KeyError:
        config = load_config_from_file()

    bus.download_bus_stop_info()

    app = dash.Dash(__name__)
    app.layout = create_app_layout(config)
    create_app_callbacks(app, config)

    # Use Minty CSS
    app.css.append_css({"external_url": CSS_DICT['minty']})
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
