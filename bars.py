import json
import codecs
import math
import sys
import argparse
# import os
import os.path
from pathlib import Path


def load_json(file_path):
    json_file = codecs.open(file_path, 'r', 'utf-8')
    bars = json_file.read()
    json_file.close()
    return json.loads(bars)["features"]


def get_biggest_bar(bars):
    return max(bar["properties"]["Attributes"]["SeatsCount"] for bar in bars)


def get_smallest_bar(bars):
    return min(bar["properties"]["Attributes"]["SeatsCount"] for bar in bars)


def get_closest_bar(bars, longitude, latitude):
    coordinates = bars[0]["geometry"]["coordinates"]
    min_distance = calculate_distance(latitude, longitude, coordinates[1], coordinates[0])
    min_bar = bars[0]
    for bar in bars:
        coordinates = bar["geometry"]["coordinates"]
        distance = calculate_distance(latitude, longitude, coordinates[1], coordinates[0])
        if distance < min_distance:
            min_distance = distance
            min_bar = bar
    bar_name = min_bar["properties"]["Attributes"]["Name"]
    latitude_final = min_bar["geometry"]["coordinates"][0]
    longitude_final = min_bar["geometry"]["coordinates"][1]
    return bar_name + "(" + str(latitude_final) + " " + str(longitude_final) + ")"


def calculate_distance(from_x, from_y, to_x, to_y):
    return math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2)


def input_float():
    user_input = input()
    try:
        return float(user_input)
    except ValueError:
        print("error: value not number")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="bars", help="custom bars data file path")
    args = parser.parse_args()

    bars_path = args.bars
    if bars_path == None:
        bars_path = "bars.json"
    print("using bars file: " +  bars_path)

    if not os.path.isfile(bars_path):
        print("error: can't find file " + bars_path)
        sys.exit()

    bar_list = load_json(bars_path)
    smallest = get_smallest_bar(bar_list)
    print("smallest bar: " + str(smallest))
    biggest = get_biggest_bar(bar_list)
    print("biggest bar: " + str(biggest))
    print("please input your coordinates to get nearest bar name")
    print("enter latitude:")
    input_latitude = input_float()
    print("enter longitude:")
    input_longitude = input_float()
    closest = get_closest_bar(bar_list, input_longitude, input_latitude)
    print("closest bar: " + closest)
    
        

    
