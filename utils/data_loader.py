import json


def load_test_data():
    with open("config/test_data.json") as file:
        return json.load(file)


def get_test_data(key):
    data = load_test_data()
    return data.get(key)