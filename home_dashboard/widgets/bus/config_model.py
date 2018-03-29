from schematics.types import StringType, IntType

from ..base import BaseWidgetModel


class BusWidgetModel(BaseWidgetModel):
    bus_stop_code = StringType(required=True)
    max_listings = IntType(default=4)
    walk_minutes_to_stop = IntType(default=5)  # Highlight buses you can catch by walking to the stop
    run_minutes_to_stop = IntType(default=2)  # Highlight buses you can catch by running to the stop
