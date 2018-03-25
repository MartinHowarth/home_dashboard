from schematics.models import Model
from schematics.types import StringType


class Train(Model):
    nre_api_key = StringType()
    train_station_code = StringType()
