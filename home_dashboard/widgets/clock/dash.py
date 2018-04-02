import dash_html_components as html
import pystache

from home_dashboard.constants import JAVASCRIPT_DIR
from home_dashboard.html_toolkit import layouts
from home_dashboard.widgets.base import BaseWidget

from .config_model import ClockWidgetModel


time_id_template = 'clockTimeElement{}'
date_id_template = 'clockDateElement{}'


def generate_clock_div(config: ClockWidgetModel):
    time_id = time_id_template.format(config.id)
    date_id = date_id_template.format(config.id)
    return layouts.create_equal_row([
        html.H1(
            className="text-center",
            id=time_id,
        ),
        html.H1(
            className="text-center",
            id=date_id,
        ),
    ])


class ClockWidget(BaseWidget):
    html_div_function = generate_clock_div
    javascript_template = 'clock.js.mustache'

    @property
    def javascript(self):
        kwargs = {
            'clockID': self.config.id,
            'clockTimeElementID': time_id_template.format(self.config.id),
            'clockDateElementID': date_id_template.format(self.config.id),
        }
        with open(self.javascript_template) as file:
            js = pystache.render(file.read(), kwargs)
        with open()
        # render javascript templates from the python code
        #  - make the 'id's match up.
        return

