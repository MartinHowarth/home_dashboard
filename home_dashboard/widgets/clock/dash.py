import dash_html_components as html
import datetime
import pytz

from home_dashboard.html_toolkit import layouts


def generate_clock_div():
    return layouts.create_equal_row([
        html.H1(
            className="text-center",
            id='clockTime',
        ),
        html.H1(
            # datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%d-%b-%Y'),
            className="text-center",
            id='clockDate',
        ),
    ])
