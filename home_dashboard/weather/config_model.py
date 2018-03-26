from schematics.models import Model
from schematics.types import StringType


class WeatherWidget(Model):
    open_weather_map_api_key = StringType(required=True)
    location = StringType(required=True)
