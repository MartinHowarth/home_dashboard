from schematics.models import Model
from schematics.types import ModelType, URLType

from home_dashboard.widgets.birthday.config_model import BirthdayWidgetModel
from home_dashboard.widgets.bus.config_model import BusWidgetModel
from home_dashboard.widgets.clock.config_model import ClockWidgetModel
from home_dashboard.widgets.train.config_model import TrainWidgetModel
from home_dashboard.widgets.weather.config_model import WeatherWidgetModel
from home_dashboard.widgets.wifi.config_model import WifiWidgetModel


class HomeDashboard(Model):
    birthday = ModelType(BirthdayWidgetModel)
    bus = ModelType(BusWidgetModel)
    clock = ModelType(ClockWidgetModel)
    train = ModelType(TrainWidgetModel)
    weather = ModelType(WeatherWidgetModel)
    wifi = ModelType(WifiWidgetModel)

    css_cdn = URLType(default='https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/minty/bootstrap.min.css')
