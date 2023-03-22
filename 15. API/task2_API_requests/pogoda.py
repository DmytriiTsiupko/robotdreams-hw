import requests
from pprint import pprint

while True:
    city = input("Введіть назву міста: ")

    # Отримання координат міста за допомогою API open-meteo.com
    response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
    if response.status_code == 200:
        data = response.json()
        # pprint(data)
        # print(data['results'][0]['latitude'])

        if 'error' in data:
            print(f"Помилка: {data['error']['message']}")
        else:
            lat, lon = data['results'][0]['latitude'], data['results'][0]['longitude']
            # Отримання поточних показників погоди за допомогою API open-meteo.com
            response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true')
            if response.status_code == 200:
                data = response.json()
                if 'error' in data:
                    print(f"Помилка: {data['error']['message']}")
                else:
                    current_weather = data['current_weather']
                    temperature = current_weather['temperature']
                    time = current_weather['time']
                    windspeed = current_weather['windspeed']
                    print(f"Погода в місті {city}.\nЧас: {time}\nТемпература: {temperature}°C\nШвидкість вітру: {windspeed} м/с\n")
            else:
                print("Помилка при отриманні даних погоди")
    else:
        print("Помилка при отриманні координат міста")