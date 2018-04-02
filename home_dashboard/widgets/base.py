from abc import ABC
from schematics.models import Model
from schematics.types import StringType


class BaseWidgetModel(Model):
    id = StringType()


class BaseWidget(ABC):
    html_div_function = None

    def __init__(self, config):
        self.config = config

    @property
    def html_div(self):
        return self.html_div_function(self.config)

    @property
    def javascript(self):
        return
