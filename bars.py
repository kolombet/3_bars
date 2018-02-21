import json
from pathlib import Path
import codecs
import math


def load_data(filepath):
    is_file = Path(filepath).is_file()
    if not is_file:
        print("file not found")
        return -1
    file = codecs.open(filepath, 'r', 'utf-8')
    data = file.read()
    file.close()
    return json.loads(data)
    pass


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
    min_distance = math.sqrt((coordinates[0] - latitude) ** 2 + (coordinates[1] - longitude) ** 2)
    min_bar = bars[0]
    for bar in bars:
        coordinates = bar["geometry"]["coordinates"]
        distance = math.sqrt((coordinates[0] - latitude) ** 2 + (coordinates[1] - longitude) ** 2)
        if distance < min_distance:
            min_distance = distance
            min_bar = bar
    return min_bar["properties"]["Attributes"]["Name"]


def calculate_distance(from_x, from_y, to_x, to_y):
    return math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2)


if __name__ == '__main__':
    bar_data = load_data("data.json")
    if bar_data:
        smallest = get_smallest_bar(bar_data)
        print("smallest bar: " + smallest)
        biggest = get_biggest_bar(bar_data)
        print("biggest bar: " + biggest)
        closest = get_closest_bar(bar_data, 55.856233, 37.584603)
        print("closest bar: " + closest)
    pass
