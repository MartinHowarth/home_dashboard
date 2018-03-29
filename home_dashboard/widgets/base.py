from schematics.models import Model
from schematics.types import StringType


class BaseWidgetModel(Model):
    id = StringType()
