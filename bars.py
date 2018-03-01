import json
import codecs
import math
import sys
import argparse
import os.path


def load_json(file_path):
    with codecs.open(file_path, "r", "utf-8") as json_file:
        bars = json_file.read()
        json_file.close()
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


def print_nearest_bar(bar_list):
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
    closest = get_closest_bar(bar_list, input_longitude, input_latitude)
    print("closest bar: {0}({1} {2})".format(get_name(closest),
          str(get_longitude(closest)), str(get_latitude(closest))))


def get_bars_path():
    parser = argparse.ArgumentParser()
    help = "custom bars data file path"
    parser.add_argument("-f", "--file", dest="bars", help="help")
    args = parser.parse_args()
    bars_path = args.bars
    if bars_path is None:
        bars_path = "bars.json"
    return bars_path


def print_bar_size(bar_list):
    template = "bar name {}, seats count {}"
    print("smallest bar:")
    bar = get_smallest_bar(bar_list)
    print(template.format(get_name(bar), str(get_seats_count(bar))))
    print("biggest bar:")
    bar = get_biggest_bar(bar_list)
    print(template.format(get_name(bar), str(get_seats_count(bar))))


if __name__ == "__main__":
    bars_path = get_bars_path()

    if not os.path.isfile(bars_path):
        print("error: can't find file {}".format(bars_path))
        sys.exit()

    bars = load_json(bars_path)
    print_bar_size(bars)
    if not print_nearest_bar(bars):
        print("error: bad value, please input number")
        sys.exit()
