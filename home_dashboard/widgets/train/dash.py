import dash_html_components as html

from .api import get_station_board
from .config_model import TrainWidgetModel


def generate_train_departures_header(station_board):
    return html.H3(children='{}'.format(station_board))


def _generate_service_row(service):
    class_name_mapping = {
        "On time": "table-primary",
        "Delayed": "table-warning",
        "Cancelled": "table-danger",
    }

    return html.Tr(
            [
                html.Td(service.destination_text),
                html.Td(service.std),
                html.Td(service.etd)
            ],
            className=class_name_mapping.get(service.etd, "table-warning")
        )


def generate_train_departures_table(train_services):
    headers = ('Destination', 'Scheduled', 'Estimated')

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in headers])] +

        # Body
        [_generate_service_row(serv) for serv in train_services],
        className="table table-condensed"
    )


def generate_train_departures_div(config: TrainWidgetModel):
    board = get_station_board(config.train_station_code, config.nre_api_key)

    train_services = board.train_services
    train_services = train_services[:config.max_listings]

    return html.Div(
        children=[
            generate_train_departures_header(board),
            generate_train_departures_table(train_services)
        ],
    )
