import requests
import random
import time

url_dict = {"Google": "https://google.com",
            "Facebook": "https://facebook.com",
            "Twitter": "https://twitter.com",
            "Amazon": "https://amazon.com",
            "Apple": "https://apple.com"}


def random_url_value(input_value: dict):
    list_values = list(input_value.keys())
    random_value = random.choice(list_values)
    res = requests.get(f"{input_value[random_value]}")
    print(f"Status code: {res.status_code}\nName: \"{random_value}\"\nLen of URL: {len(input_value[random_value])}")


if __name__ == '__main__':
    start = time.time()
    random_url_value(url_dict)
    end = time.time() - start
    print(f"Request execution time: {end} sec")
