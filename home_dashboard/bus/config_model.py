from schematics.models import Model
from schematics.types import StringType


class Bus(Model):
    bus_stop_code = StringType()
