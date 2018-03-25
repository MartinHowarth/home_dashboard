from schematics.models import Model
from schematics.types import ModelType, ListType

from home_dashboard.birthday.config_model import Birthday
from home_dashboard.bus.config_model import Bus
from home_dashboard.train.config_model import Train
from home_dashboard.weather.config_model import Weather


class HomeDashboard(Model):
    birthdays = ListType(ModelType(Birthday))
    bus = ModelType(Bus)
    train = ModelType(Train)
    weather = ModelType(Weather)
