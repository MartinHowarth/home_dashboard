from schematics.models import Model
from schematics.types import StringType, DateType, ListType, ModelType, IntType

from ..base import BaseWidgetModel


class BirthdayModel(Model):
    name = StringType(required=True)
    date = DateType(required=True)


class BirthdayWidgetModel(BaseWidgetModel):
    birthdays = ListType(ModelType(BirthdayModel))
    max_listings = IntType(default=4)

