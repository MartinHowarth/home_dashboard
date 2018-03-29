from schematics.types import StringType, URLType

from ..base import BaseWidgetModel

RAIN_ICON_URL = "https://www.freeiconspng.com/uploads/weather-icon-png-19.png"
SUN_ICON_URL = ("https://pre00.deviantart.net/1125/th/pre/i/2014/153/2/3/"
                "praise_the_sun_solaire_chibi_by_james23x-d7krxjf.png")


class WeatherWidgetModel(BaseWidgetModel):
    open_weather_map_api_key = StringType(required=True)
    location = StringType(required=True)

    sunny_image_url = URLType(default=SUN_ICON_URL)
    rainy_image_url = URLType(default=RAIN_ICON_URL)
