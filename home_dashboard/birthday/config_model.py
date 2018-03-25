from schematics.models import Model
from schematics.types import StringType, DateType


class Birthday(Model):
    name = StringType()
    date = DateType()
