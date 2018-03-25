import dash_html_components as html
import datetime
import pytz


def generate_clock_div():
    return html.Div(
        [
            html.Div(children=[
                html.H1(
                    datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%H:%M:%S'),
                    className="display-1"
                )],
                className="text-left",
            ),
            html.Div(children=[
                html.H4(
                    datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%d-%b-%Y'),
                    className="display-1"
                )],
                className="text-right",
            ),
        ],
        className="d-flex justify-content-between"
    )
