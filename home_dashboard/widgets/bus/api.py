import csv
import requests
import string
import math
import munch
import os

from operator import attrgetter
from typing import List
from pathlib import Path

CSV_FILENAME = os.path.join(str(Path.home()), 'tfl_bus_stops.csv')


def download_bus_stop_info():
    url = 'http://data.tfl.gov.uk/tfl/syndication/feeds/bus-stops.csv?app_id=&app_key='
    r = requests.get(url)

    r.raise_for_status()

    csv_file = r.content.decode("utf-8")

    # Remove unprintable characters before writing to file
    filtered_string = ''.join(filter(lambda x: x in string.printable, csv_file))

    with open(CSV_FILENAME, 'w') as fi:
        fi.write(filtered_string)


def get_bus_stop_details(match_key: str, match_value: str, desired_key: str) -> str:
    with open(CSV_FILENAME) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        first_line = next(reader)
        column_map = {key: ii for ii, key in enumerate(first_line)}

        try:
            match_column = column_map[match_key]
        except KeyError:
            raise KeyError("match_key not found in csv")

        try:
            desired_column = column_map[desired_key]
        except KeyError:
            raise KeyError("desired_key not found in csv")

        for row in reader:
            if row and str(row[match_column]) == match_value:
                return row[desired_column]
    raise ValueError("match_value not found")


def get_bus_stop_live_info(naptan_id: str) -> List[munch.Munch]:
    url = 'https://api.tfl.gov.uk/StopPoint/{}/arrivals'.format(naptan_id)
    r = requests.get(url)
    r.raise_for_status()

    arrivals = []
    for arrival in r.json():
        arrival['minutesToStation'] = math.floor(arrival['timeToStation'] / 60)
        arrivals.append(munch.Munch(arrival))

    arrivals = sorted(arrivals, key=attrgetter('timeToStation'))

    return arrivals


def get_bus_stop_live_arrivals_by_stop_code(bus_stop_code):
    naptan_id = get_bus_stop_details('Bus_Stop_Code', bus_stop_code, 'Naptan_Atco')
    return get_bus_stop_live_info(naptan_id)


def get_bus_stop_name_by_stop_code(bus_stop_code):
    return get_bus_stop_details('Bus_Stop_Code', bus_stop_code, 'Stop_Name')
