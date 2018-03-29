import dash_html_components as html
import datetime
import pytz

from home_dashboard.gui import grid


def generate_clock_div():
    return grid.create_equal_row([
        html.H1(
            datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%H:%M:%S'),
            className="text-center",
        ),
        html.H1(
            datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%d-%b-%Y'),
            className="text-center"
        )
    ])
