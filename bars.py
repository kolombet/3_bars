import json
import codecs
import math
import sys
import argparse
import os.path


def load_json(file_path):
    with codecs.open(file_path, "r", "utf-8") as json_file:
        bars = json_file.read()
        return json.loads(bars)["features"]


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


def request_coordinates():
    print("please input your coordinates to get nearest bar name")
    print("enter longitude:")
    try:
        input_longitude = float(input())
    except ValueError:
        return None
    print("enter latitude:")
    try:
        input_latitude = float(input())
    except ValueError:
        return None
    return dict(
        longitude=input_longitude,
        latitude=input_latitude
    )


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        dest="bars",
        help="custom bars data file path",
        default="bars.json")
    return parser.parse_args()


def print_bar(bar):
    template = "bar name: {}, seats count: {}, coordinates: {}"
    formatted = template.format(
        get_name(bar),
        str(get_seats_count(bar)),
        str(get_longitude(bar)),
        str(get_latitude(bar))
    )
    print(formatted)


if __name__ == "__main__":
    bars_path = get_args().bars

    if not os.path.isfile(bars_path):
        sys.exit("error: can't find file {}".format(bars_path))

    bars = load_json(bars_path)

    print("smallest bar:")
    print_bar(get_smallest_bar(bar_list))
    print("biggest bar:")
    print_bar(get_biggest_bar(bar_list))

    coordinates = request_coordinates()
    if not coordinates:
        sys.exit("error: bad value, please input number")
    closest_bar = get_closest_bar(
        bars,
        coordinates["longitude"],
        coordinates["latitude"]
    )
    print_bar(closest_bar)
