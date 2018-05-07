from schematics.types import ListType, StringType, ModelType
from schematics.models import Model
from typing import List  # NOQA

from ..base import BaseWidgetModel


class VisitorBookEntryModel(Model):
    author = StringType(required=True)
    text = StringType(required=True)


class VisitorBookWidgetModel(BaseWidgetModel):
    entries = ListType(ModelType(VisitorBookEntryModel), required=True)  # type: List[VisitorBookEntryModel]
    link = 'http://127.0.0.1:90'
