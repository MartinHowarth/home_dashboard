from schematics.models import Model
from schematics.types import StringType, IntType


class TrainWidget(Model):
    nre_api_key = StringType(required=True)
    train_station_code = StringType(required=True)
    max_listings = IntType(default=4)
