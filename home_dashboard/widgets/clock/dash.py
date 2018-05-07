import dash_html_components as html

from home_dashboard.html_toolkit import layouts
from home_dashboard.widgets.base import BaseWidget, render_javascript_template, make_full_filepath

from .config_model import ClockWidgetModel


time_id_template = 'clockTimeElement{}'
date_id_template = 'clockDateElement{}'
js_loop_name_template = 'updateClock{}'


def generate_clock_div(config: ClockWidgetModel):
    return layouts.create_equal_row([
        html.H1(
            className="text-center",
            id=time_id_template.format(config.id),
        ),
        html.H1(
            className="text-center",
            id=date_id_template.format(config.id),
        ),
    ])


def generate_clock_javascript(config: ClockWidgetModel):
    render_javascript_template(
        make_full_filepath(__file__, 'clock.js.mustache'),
        config.id,
        {
            'clockTimeElementID': time_id_template.format(config.id),
            'clockDateElementID': date_id_template.format(config.id),
            'loopName': js_loop_name_template.format(config.id)
        }
    )


class ClockWidget(BaseWidget):
    html_div_function = generate_clock_div
    generate_javascript_function = generate_clock_javascript

    @property
    def js_initial_function_names(self):
        return [js_loop_name_template.format(self.config.id)]
