from schematics.models import Model
from schematics.types import ModelType

from home_dashboard.gui.config_model import DashboardGuiModel
from home_dashboard.widgets.birthday.config_model import BirthdayWidgetModel
from home_dashboard.widgets.bus.config_model import BusWidgetModel
from home_dashboard.widgets.train.config_model import TrainWidgetModel
from home_dashboard.widgets.weather.config_model import WeatherWidgetModel
from home_dashboard.widgets.wifi.config_model import WifiWidgetModel


class HomeDashboardModel(Model):
    birthday = ModelType(BirthdayWidgetModel)
    bus = ModelType(BusWidgetModel)
    train = ModelType(TrainWidgetModel)
    weather = ModelType(WeatherWidgetModel)
    wifi = ModelType(WifiWidgetModel)

    gui = ModelType(DashboardGuiModel)
