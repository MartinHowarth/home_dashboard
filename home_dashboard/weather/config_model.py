from schematics.models import Model
from schematics.types import StringType


class Weather(Model):
    open_weather_map_api_key = StringType()
    location = StringType()
