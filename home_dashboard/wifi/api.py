import os
import wifi_qrcode_generator

from .config_model import WifiWidget


QR_IMG_PATH = os.path.expanduser('~/wifi_qr.png')


def generate_wifi_qr_code(config: WifiWidget):
    qr_code = wifi_qrcode_generator.wifi_qrcode(
      config.ssid, False, config.auth_type, config.password#, box_size=5
    )
    qr_code.save(QR_IMG_PATH)
