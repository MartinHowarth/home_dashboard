import dash_html_components as html
import pyqrcode
import random
import os

from home_dashboard.html_toolkit import layouts
from home_dashboard.widgets.base import BaseWidget

from .config_model import VisitorBookWidgetModel

QR_IMG_PATH = os.path.expanduser('~/visitor_book_qr.png')


def generate_visitor_book_qr_code_base64(config: VisitorBookWidgetModel):
    url = pyqrcode.create(config.link)
    return url.png_as_base64_str(scale=8, quiet_zone=0)


def generate_visitor_book_div(config: VisitorBookWidgetModel):
    message_to_display = random.choice(config.entries)

    grid_elements = [
        layouts.GridElement(
            html.Div(
                children=[
                    html.Button(
                        'Leave a message!',
                        className="btn btn-info mb-1 mt-5 d-block mx-auto"
                    ),
                    html.Img(
                        src='data:image/png;base64,{}'.format(generate_visitor_book_qr_code_base64(config)),
                        className='d-block align-middle mx-auto mb-5',
                        style={'width': '40%'}
                    ),
                ]
            ),
            4
        ),
        layouts.GridElement(
            html.Div(
                children=[
                    html.H4(
                        message_to_display.author,
                        className='card-header text-center'
                    ),
                    html.H2(
                        message_to_display.text,
                        className='card-body text-center'
                    )
                ],
                className="card text-white bg-info mt-5 mb-5",
            ),
            8
        ),
    ]

    return layouts.create_weighted_row(
        grid_elements
    )


class VisitorBookWidget(BaseWidget):
    html_div_function = generate_visitor_book_div
