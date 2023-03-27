import requests


class Pogoda:

    geocoding_api_open_meteo = "https://geocoding-api.open-meteo.com/v1/search?name="

    def __init__(self, city: str):
        self.city = city
        self.session = requests.Session()

    # Отримання координат міста за допомогою API
    def get_cord(self):
        response = self.session.get(f"{self.geocoding_api_open_meteo}{self.city}")

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Other error occurred: {err}")
        else:
            data = response.json()
            return data.get("results", "Помилка при отриманні координат міста")

    def get_weather_by_cord(self):
        cord_data = self.get_cord()
        if not isinstance(cord_data, str):
            lat, lon = cord_data[0]["latitude"], cord_data[0]["longitude"]
            response = self.session.get(
                f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            )

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred: {err}")
            except requests.exceptions.RequestException as err:
                print(f"Other error occurred: {err}")
            else:
                cord_data = response.json()

            try:
                current_weather = cord_data["current_weather"]
                temperature = current_weather["temperature"]
                time = current_weather["time"]
                windspeed = current_weather["windspeed"]
                print(
                    f"Погода в місті {self.city}.\nЧас: {time}\n"
                    f"Температура: {temperature}°C\n"
                    f"Швидкість вітру: {windspeed} м/с\n"
                )
            except KeyError as key_error:
                print(f"Key Error: {key_error}")
        else:
            print(cord_data)


if __name__ == "__main__":
    while True:
        local_weather = Pogoda(input("Введіть назву міста: ").strip().capitalize())
        local_weather.get_weather_by_cord()

