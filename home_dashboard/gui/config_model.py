from schematics.models import Model
from schematics.types import ListType, ModelType, StringType, URLType

from typing import List


class GridElementModel(Model):
    id = StringType(required=True)


class RowModel(Model):
    elements = ListType(ModelType(GridElementModel))  # type: List[GridElementModel]


class GridModel(Model):
    rows = ListType(ModelType(RowModel))  # type: List[RowModel]


class DashboardGuiModel(Model):
    layout = ModelType(GridModel)
    css_cdn = URLType(default='https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/minty/bootstrap.min.css')
