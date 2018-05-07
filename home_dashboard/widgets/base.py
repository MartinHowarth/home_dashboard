import dash_html_components as html
import os
import pystache

from abc import ABC
from schematics.models import Model
from schematics.types import StringType
from typing import Dict

from home_dashboard.constants import JAVASCRIPT_DIR


def make_full_filepath(neighbour: str, target_file: str) -> str:
    """
    Prepend the path of neighbour to target_file.

    :param neighbour: File in the desired path location. Typically just pass in `__file__`.
    :param target_file: Path-less filename to add a path to.
    """
    return os.path.join(os.path.split(neighbour)[0], target_file)


def render_javascript_template(template_path: str, uid: str, parameters: Dict) -> None:
    with open(template_path) as file:
        js = pystache.render(file.read(), parameters)

    filename_mustache = os.path.split(template_path)[1]
    filename = os.path.splitext(filename_mustache)[0]
    filename = os.path.splitext(filename)[0] + uid + os.path.splitext(filename)[1]
    with open(os.path.join(JAVASCRIPT_DIR, filename), 'w') as file:
        file.write(js)


class BaseWidgetModel(Model):
    id = StringType()

    def validate_id(self, data, value):
        if value:
            return value
        data['id'] = self.__class__.__name__
        return self.__class__.__name__


class BaseWidget(ABC):
    html_div_function = None
    generate_javascript_function = None

    def __init__(self, config: BaseWidgetModel):
        self.config = config

    @property
    def html_div(self) -> html.Div:
        """
        Generate the html.Div dash object that represents this Widget.

        May be accessed repeatedly.
        """
        return self.__class__.html_div_function(self.config)

    def generate_javascript(self):
        """
        Generate any javascript required to run the widget to the JAVASCRIPT directory.

        This will only be called once upon app initialisation.
        """
        return self.__class__.generate_javascript_function(self.config)

    @property
    def js_initial_function_names(self):
        """
        List of any javascript function names to be called on initial page
        load (after html layout has been defined).

        For example, this is used to kick off any javascript update loops.
        """
        return []
