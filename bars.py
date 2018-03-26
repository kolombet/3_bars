import json
import codecs
import math
import sys
import argparse
import os.path


def load_bars_from_file(file_path):
    with codecs.open(file_path, "r", "utf-8") as json_file:
        return json.loads(json_file.read())["features"]


def get_biggest_bar(bars):
    return max(bars, key=lambda bar: get_seats_count(bar))


def get_smallest_bar(bars):
    return min(bars, key=lambda bar: get_seats_count(bar))


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bar: calculate_distance(
        latitude, longitude, get_latitude(bar), get_longitude(bar)))


def calculate_distance(from_x, from_y, to_x, to_y):
    return math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2)


def get_seats_count(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_name(bar):
    return bar["properties"]["Attributes"]["Name"]


def get_longitude(bar):
    return bar["geometry"]["coordinates"][1]


def get_latitude(bar):
    return bar["geometry"]["coordinates"][0]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        dest="bars",
        help="custom bars data file path",
        default="bars.json")
    return parser.parse_args()


def format_bar(label, bar):
    template = "{} - bar name: {}, seats count: {}, coordinates: ({}, {})"
    return template.format(
        label,
        get_name(bar),
        get_seats_count(bar),
        get_longitude(bar),
        get_latitude(bar)
    )


def print_info(smallest_bar, biggest_bar, closest_bar):
    print(format_bar("smallest bar:", smallest_bar))
    print(format_bar("biggest bar:", biggest_bar))
    print(format_bar("closest bar:", closest_bar))


def request_coordinates():
    print("""To get nearest bar name please input your coordinates -
longitude and latitude in format {longitude},{latitude}.
(values must be separated by comma)""")
    separator = ","
    try:
        input_string = input()
        coordinates = input_string.split(separator)
        return dict(
            longitude=float(coordinates[0]),
            latitude=float(coordinates[1])
        )
    except ValueError:
        return None


if __name__ == "__main__":
    bars_path = get_args().bars

    if not os.path.isfile(bars_path):
        sys.exit("error: can't find file {}".format(bars_path))

    bars_features = load_bars_from_file(bars_path)
    user_coordinates = request_coordinates()
    if not user_coordinates:
        sys.exit("error: bad value")
    closest_bar = get_closest_bar(
        bars_features,
        user_coordinates["longitude"],
        user_coordinates["latitude"]
    )
    smallest_bar = get_smallest_bar(bars_features)
    biggest_bar = get_biggest_bar(bars_features)
    print_info(smallest_bar, biggest_bar, closest_bar)
