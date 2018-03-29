from schematics.types import StringType

from ..base import BaseWidgetModel


class WifiWidgetModel(BaseWidgetModel):
    auth_type = StringType(default='WPA')
    password = StringType(required=True)
    ssid = StringType(required=True)
