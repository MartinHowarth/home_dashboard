import requests
import pytz

from datetime import datetime, timedelta

from .config_model import WeatherWidgetModel


RAIN_MM_THRESHOLD = 1


def filter_to_current_day(forecast_list):
    utcnow = datetime.now(pytz.timezone('Europe/London'))

    if utcnow.hour >= 21:
        target_date = (utcnow + timedelta(days=1)).date()
    else:
        target_date = utcnow.date()

    def forecast_date(forecast_dict):
        return datetime.fromtimestamp(forecast_dict['dt']).date()

    return list(filter(lambda x: (forecast_date(x) == target_date), forecast_list))


def is_significant_rain(forecast_list):
    rain_mm = sum((float(fc.get('rain', {}).get('3h', 0)) for fc in forecast_list))
    return rain_mm > RAIN_MM_THRESHOLD


def get_weather_icon_url(config: WeatherWidgetModel):
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'
                     .format(config.location, config.open_weather_map_api_key))
    r.raise_for_status()

    forecast_list = r.json()['list']
    forecast_list = filter_to_current_day(forecast_list)

    if is_significant_rain(forecast_list):
        icon_url = config.rainy_image_url
    else:
        icon_url = config.sunny_image_url
    return icon_url
