import dash_html_components as html

from .config_model import WeatherWidgetModel
from .api import get_weather_icon_url


def generate_weather_div(config: WeatherWidgetModel):
    return html.Div(
        children=[
            html.Img(
                src=get_weather_icon_url(config),
                style={'display': 'block',
                       'width': '100%',
                       'vertical-align': 'middle'}
            ),
        ],
    )
