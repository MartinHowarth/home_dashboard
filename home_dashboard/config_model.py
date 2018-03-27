from schematics.models import Model
from schematics.types import ModelType

from home_dashboard.birthday.config_model import BirthdayWidget
from home_dashboard.bus.config_model import BusWidget
from home_dashboard.train.config_model import TrainWidget
from home_dashboard.weather.config_model import WeatherWidget
from home_dashboard.wifi.config_model import WifiWidget


class HomeDashboard(Model):
    birthday = ModelType(BirthdayWidget)
    bus = ModelType(BusWidget)
    train = ModelType(TrainWidget)
    weather = ModelType(WeatherWidget)
    wifi = ModelType(WifiWidget)
