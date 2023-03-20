import requests
import random
import timeit

links = {"Google": "https://google.com",
         "Facebook": "https://facebook.com",
         "Twitter": "https://twitter.com",
         "Amazon": "https://amazon.com",
         "Apple": "https://apple.com"}


def random_list_value(input_value: dict):
    list_values = list(input_value.keys())
    random_value = random.choice(list_values)
    res = requests.get(f"{input_value[random_value]}")
    print(f"Status code: {res.status_code}\nName: \"{random_value}\"\nLen of URL: {len(input_value[random_value])}")


if __name__ == '__main__':
    random_list_value(links)
