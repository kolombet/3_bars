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
    bar_data = json_file.read()
    json_file.close()
    return json.loads(bar_data)


def get_biggest_bar(data):
    bars = data["features"]
    max_value = bars[0]["properties"]["Attributes"]["SeatsCount"]
    max_bar = bars[0]
    for bar in bars:
        count = bar["properties"]["Attributes"]["SeatsCount"]
        if count > max_value:
            max_value = count
            max_bar = bar
    return max_bar["properties"]["Attributes"]["Name"]


def get_smallest_bar(data):
    bars = data["features"]
    min_value = bars[0]["properties"]["Attributes"]["SeatsCount"]
    min_bar = bars[0]
    for bar in bars:
        count = bar["properties"]["Attributes"]["SeatsCount"]
        # if zero places in bar - it's wrong data or imaginary bar
        if count != 0 and count < min_value:
            min_value = count
            min_bar = bar
    return min_bar["properties"]["Attributes"]["Name"]


def get_closest_bar(data, longitude, latitude):
    bars = data["features"]
    coordinates = bars[0]["geometry"]["coordinates"]
    min_distance = calculate_distance(coordinates[0], latitude, coordinates[1], longitude)
    min_bar = bars[0]
    for bar in bars:
        coordinates = bar["geometry"]["coordinates"]
        distance = calculate_distance(coordinates[0], latitude, coordinates[1], longitude)
        if distance < min_distance:
            min_distance = distance
            min_bar = bar
    return min_bar["properties"]["Attributes"]["Name"]


def calculate_distance(from_x, from_y, to_x, to_y):
    return math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2)

def request_float():
    user_input = input()
    try:
        float(user_input)
    except ValueError:
        print "value not number - please try again"
        return request_float()
    
if __name__ == '__main__':
    bar_data = load_data("bar-data.json")
    if bar_data:
        smallest = get_smallest_bar(bar_data)
        print("smallest bar: " + smallest)
        biggest = get_biggest_bar(bar_data)
        print("biggest bar: " + biggest)
        print("please input your coordinates to get nearest bar name")
        print("enter latitude:")
        input_latitude = request_float()
        print("enter longitude:")
        input_longitude = request_float()
        closest = get_closest_bar(bar_data, input_latitude, input_longitude)
        print("closest bar: " + closest)
    pass
