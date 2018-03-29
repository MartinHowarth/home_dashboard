import dash_html_components as html

from .config_model import GridModel
from .grid import create_equal_grid


def generate_layout(config: GridModel):
    # Convert each element in the grid to a HTML object
    html_rows = []
    for row in config.rows:
        html_row = []
        for element in row:
            html_element = html.Div(id=element.id)
            html_row.append(html_element)
        html_rows.append(html_row)

    html_grid = create_equal_grid(html_rows)
    return html_grid
