import dash_html_components as html

from .config_model import BirthdayWidget

from datetime import date

MAX_DAYS_TO_BIRTHDAY = 28
WARNING_DAYS = 7


def days_to_next_date(target_date: date) -> int:
    today = date.today()
    target_date = date(today.year, target_date.month, target_date.day)

    days_to_go = (target_date - today).days

    # If the birthday is earlier in the year then the current date, then check against next year.
    if days_to_go < 0:
        target_date = date(today.year + 1, target_date.month, target_date.day)
        days_to_go = (target_date - today).days

    return days_to_go


def is_soon_enough(birthday: BirthdayWidget) -> bool:
    return days_to_next_date(birthday.date) < MAX_DAYS_TO_BIRTHDAY


def generate_upcoming_birthdays_header():
    return html.H3(children='Upcoming Birthdays')


def _generate_birthday_row(birthday: BirthdayWidget):
    is_today = days_to_next_date(birthday.date) == 0

    class_name = "table-default"
    if is_today:
        class_name = "table-success"
    elif days_to_next_date(birthday.date) <= WARNING_DAYS:
        class_name = "table-primary"

    return html.Tr(
        [
            html.Td(birthday.name),
            html.Td(birthday.date),
            html.Td(days_to_next_date(birthday.date) if not is_today else "TODAY!")
        ],
        className=class_name
    )


def generate_upcoming_birthdays_table(config: BirthdayWidget):
    headers = ('Name', 'Date', 'Days')

    ordered_birthdays = sorted(config.birthdays, key=lambda x: days_to_next_date(x.date))
    ordered_birthdays = ordered_birthdays[:config.max_listings]

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in headers])] +

        # Body
        [_generate_birthday_row(birthday) for birthday in ordered_birthdays if is_soon_enough(birthday)],
        className="table table-condensed"
    )


def generate_upcoming_birthdays_div(config):
    return html.Div(
        children=[
            generate_upcoming_birthdays_header(),
            generate_upcoming_birthdays_table(config)
        ],
    )
