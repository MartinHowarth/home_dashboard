# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import importlib
import os
import sys

from home_dashboard import bus, birthday, train

from home_dashboard.config_model import HomeDashboard

CSS_DICT = {
    'minty': 'https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/minty/bootstrap.min.css'
}


def load_config_from_file() -> HomeDashboard:
    # Strip the .py extension
    config_file = os.path.splitext(sys.argv[1])[0]
    config_module = importlib.import_module(config_file)

    return HomeDashboard(config_module.config)


def create_app_layout(_config: HomeDashboard):
    train_bus_row = html.Div(
        children=[
            bus.generate_bus_arrivals_div(_config.bus),
            train.generate_train_departures_div(_config.train),
        ],
        className="row"
    )

    def regenerate_layout():
        return html.Div(
            children=[
                train_bus_row,
                birthday.generate_upcoming_birthdays_div(_config.birthdays),
            ],
            className="container"
        )
    return regenerate_layout


if __name__ == "__main__":
    config = load_config_from_file()

    bus.download_bus_stop_info()

    app = dash.Dash()
    app.layout = create_app_layout(config)

    # Use Minty CSS
    app.css.append_css({"external_url": CSS_DICT['minty']})
    app.run_server(debug=True)
