import dash_html_components as html

from .api import get_bus_stop_live_arrivals_by_stop_code, get_bus_stop_name_by_stop_code
from .config_model import BusWidget


def generate_bus_arrivals_header(bus_stop_name):
    return html.H3(children='Bus Arrivals ({})'.format(bus_stop_name))


def _generate_bus_arrival_row(config, arrival):
    body_element_keys = ('lineName', 'towards', 'minutesToStation')

    if arrival['minutesToStation'] <= config.run_minutes_to_stop:
        class_name = "table-warning"
    elif arrival['minutesToStation'] <= config.walk_minutes_to_stop:
        class_name = "table-success"
    else:
        class_name = "table-default"

    return html.Tr(
        [html.Td(arrival[key]) for key in body_element_keys],
        className=class_name
    )


def generate_bus_arrivals_table(config, arrivals):
    headers = ('Route', 'Towards', 'Minutes')

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in headers])] +

        # Body
        [_generate_bus_arrival_row(config, arr) for arr in arrivals],
        className="table table-condensed"
    )


def generate_bus_arrivals_div(config: BusWidget):
    arrivals = get_bus_stop_live_arrivals_by_stop_code(config.bus_stop_code)
    bus_stop_name = get_bus_stop_name_by_stop_code(config.bus_stop_code)

    arrivals = arrivals[:config.max_listings]

    return html.Div(
        children=[
            generate_bus_arrivals_header(bus_stop_name),
            generate_bus_arrivals_table(config, arrivals)
        ],
    )
