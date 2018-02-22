import json
from pathlib import Path
import codecs
import math


def load_data(filepath):
    is_file = Path(filepath).is_file()
    if not is_file:
        print("file not found")
        return -1
    json_file = codecs.open(filepath, 'r', 'utf-8')
    bars = json_file.read()
    json_file.close()
    return json.loads(bars)


def get_biggest_bar(data):
    return max(bar["properties"]["Attributes"]["SeatsCount"] for bar in data["features"])


def get_smallest_bar(data):
    return min(bar["properties"]["Attributes"]["SeatsCount"] for bar in data["features"])


def get_closest_bar(data, longitude, latitude):
    bars = data["features"]
    coordinates = bars[0]["geometry"]["coordinates"]
    min_distance = calculate_distance(latitude, longitude, coordinates[1], coordinates[0])
    min_bar = bars[0]
    for bar in bars:
        coordinates = bar["geometry"]["coordinates"]
        distance = calculate_distance(latitude, longitude, coordinates[1], coordinates[0])
        if distance < min_distance:
            min_distance = distance
            min_bar = bar
    return min_bar["properties"]["Attributes"]["Name"] + "(" + str(bar["geometry"]["coordinates"][0]) + " " + str(bar["geometry"]["coordinates"][1]) + ")"


def calculate_distance(from_x, from_y, to_x, to_y):
    return math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2)


def request_float():
    user_input = input()
    try:
        user_input_parsed = float(user_input)
        return user_input_parsed
    except ValueError:
        print("value not number - please try again")
        return request_float()


if __name__ == '__main__':
    bar_list = load_data("bar-data.json")
    if bar_list:
        smallest = get_smallest_bar(bar_list)
        print("smallest bar: " + str(smallest))
        biggest = get_biggest_bar(bar_list)
        print("biggest bar: " + str(biggest))
        print("please input your coordinates to get nearest bar name")
        print("enter latitude:")
        input_latitude = request_float()
        print("enter longitude:")
        input_longitude = request_float()
        closest = get_closest_bar(bar_data, input_longitude, input_latitude)
        print("closest bar: " + closest)
