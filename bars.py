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
    template = "{} - bar name: {}, seats count: {}, coordinates: ({}, {})\n"
    return template.format(
        label,
        get_name(bar),
        str(get_seats_count(bar)),
        str(get_longitude(bar)),
        str(get_latitude(bar))
    )


def print_info(bars, coordinates):
    closest_bar = get_closest_bar(
        bars,
        coordinates["longitude"],
        coordinates["latitude"]
    )
    print(format_bar("smallest bar:", get_smallest_bar(bars)))
    print(format_bar("biggest bar:", get_biggest_bar(bars)))
    print(format_bar("closest bar:", closest_bar))


def get_user_input():
    try:
        return float(input())
    except ValueError:
        return None


def request_coordinates():
    print("please input your coordinates to get nearest bar name")
    return dict(
        longitude=request_coordinate("enter longitude:"),
        latitude=request_coordinate("enter latitude")
    )


def request_coordinate(message):
    print(message)
    return get_user_input()


if __name__ == "__main__":
    bars_path = get_args().bars

    if not os.path.isfile(bars_path):
        sys.exit("error: can't find file {}".format(bars_path))

    bars = load_bars_from_file(bars_path)
    coordinates = request_coordinates()
    if not coordinates:
        sys.exit("error: bad value, please input number")
    print_info(bars, coordinates)
