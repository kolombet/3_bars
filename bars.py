import json
from pathlib import Path
import codecs


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
    pass


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
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    bar_data = load_data("data.json")
    smallest = get_smallest_bar(bar_data)
    print("smallest bar: " + smallest)
    biggest = get_biggest_bar(bar_data)
    print("biggest bar: " + biggest)
    pass
