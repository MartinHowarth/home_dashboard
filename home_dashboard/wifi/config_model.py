from schematics.models import Model
from schematics.types import StringType


class WifiWidget(Model):
    auth_type = StringType(default='WPA')
    password = StringType(required=True)
    ssid = StringType(required=True)
