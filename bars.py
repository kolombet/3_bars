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
    return min(bars, key=lambda bar: calculate_distance(latitude, longitude, get_latitude(bar), get_longitude(bar)))
    

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="bars", help="custom bars data file path")
    args = parser.parse_args()

    bars_path = args.bars
    if bars_path == None:
        bars_path = "bars.json"
    print("using bars file: {}".format(bars_path))

    if not os.path.isfile(bars_path):
        print("error: can't find file {}".format(bars_path))
        sys.exit()

    bar_list = load_json(bars_path)
    smallest = get_smallest_bar(bar_list)
    template = "{} bar name: {} seats count: {}"
    print(template.format("smallest", get_name(smallest), str(get_seats_count(smallest))))
    biggest = get_biggest_bar(bar_list)
    print(template.format("biggest", get_name(biggest), str(get_seats_count(biggest))))

    print("please input your coordinates to get nearest bar name")

    print("enter longitude:")
    try:
        input_longitude = float(input())
    except ValueError:
        print("bad longitude value (must ")
        sys.exit()

    print("enter latitude:")
    try:
        input_latitude = float(input())
    except ValueError:
        print("bad latitude value")
        sys.exit()

    closest = get_closest_bar(bar_list, input_longitude, input_latitude)
    print("closest bar: {0}({1} {2})".format(get_name(closest), str(get_longitude(closest)), str(get_latitude(closest))))
    
        

    
