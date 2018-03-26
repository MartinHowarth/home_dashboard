from schematics.models import Model
from schematics.types import StringType, DateType, ListType, ModelType, IntType


class Birthday(Model):
    name = StringType(required=True)
    date = DateType(required=True)


class BirthdayWidget(Model):
    birthdays = ListType(ModelType(Birthday))
    max_listings = IntType(default=4)

