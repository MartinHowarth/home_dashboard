import requests
import pytz

from datetime import datetime, timedelta


RAIN_MM_THRESHOLD = 1
RAIN_ICON_URL = "https://www.freeiconspng.com/uploads/weather-icon-png-19.png"
SUN_ICON_URL = ("https://pre00.deviantart.net/1125/th/pre/i/2014/153/2/3/"
                "praise_the_sun_solaire_chibi_by_james23x-d7krxjf.png")


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


def get_icon_url(icon_code):
    return "http://openweathermap.org/img/w/{}.png".format(icon_code)


def get_weather_icon_url(config):
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'
                     .format(config.location, config.open_weather_map_api_key))
    r.raise_for_status()

    forecast_list = r.json()['list']
    forecast_list = filter_to_current_day(forecast_list)

    if is_significant_rain(forecast_list):
        icon_url = RAIN_ICON_URL
    else:
        icon_url = SUN_ICON_URL
    return icon_url
