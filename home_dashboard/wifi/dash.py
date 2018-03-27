import base64
import dash_html_components as html

from .config_model import WifiWidget
from .api import QR_IMG_PATH


def generate_wifi_div(config: WifiWidget):
    # Serve the local file by base64 encoding it.
    with open(QR_IMG_PATH, 'rb') as img:
        encoded_image = base64.b64encode(img.read())

    return html.Div(
        children=[
            html.Img(
                src='data:image/png;base64,{}'.format(encoded_image.decode()),
                style={'display': 'block',
                       'width': '100%',
                       'vertical-align': 'middle'}
            ),
        ],
    )
