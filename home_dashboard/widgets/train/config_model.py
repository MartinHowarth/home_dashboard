from schematics.types import StringType, IntType

from ..base import BaseWidgetModel


class TrainWidgetModel(BaseWidgetModel):
    nre_api_key = StringType(required=True)
    train_station_code = StringType(required=True)
    max_listings = IntType(default=4)
