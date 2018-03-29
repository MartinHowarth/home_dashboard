from schematics.models import Model
from schematics.types import StringType


class BaseWidgetModel(Model):
    id = StringType()

    def validate_id(self, data, _id):
        # Set the default ID to be the class name.
        if not _id:
            _id = self.__class__.__name__
        data['id'] = _id
        return _id
