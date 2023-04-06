import requests


class WeatherAPIWrapper:
    def __init__(self):
        self.geocoding_api_url = "https://geocoding-api.open-meteo.com/v1/search?name="
        self.weather_api_url = "https://api.open-meteo.com/v1/forecast"
        self.session = requests.Session()

    def get_coordinates(self, city: str):
        response = self.session.get(f"{self.geocoding_api_url}{city}")
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            return data["results"][0]["latitude"], data["results"][0]["longitude"]
        else:
            raise ValueError("Error: Coordinates not found")

    def get_current_weather(self, lat: float, lon: float):
        response = self.session.get(f"{self.weather_api_url}?latitude={lat}&longitude={lon}&current_weather=true")
        response.raise_for_status()
        data = response.json()
        if "current_weather" in data:
            return data["current_weather"]
        else:
            raise ValueError("Error: Current weather data not found")


class Pogoda:
    def __init__(self, city: str):
        self.city = city
        self.api_wrapper = WeatherAPIWrapper()

    def get_weather(self):
        try:
            lat, lon = self.api_wrapper.get_coordinates(self.city)
            current_weather = self.api_wrapper.get_current_weather(lat, lon)
            temperature = current_weather["temperature"]
            time = current_weather["time"]
            wind_speed = current_weather["windspeed"]
            print(
                f"Weather in city {self.city}\n"
                f"Current time: {time}\nТемпература: {temperature}°C\n"
                f"Wind speed: {wind_speed} м/с\n")
        except ValueError as error:
            print(str(error))


if __name__ == "__main__":
    while True:
        value = input("Введіть назву міста: ").strip().capitalize()
        if value != 'End':
            local_weather = Pogoda(value)
            local_weather.get_weather()
        else:
            print("See y soon!")
            break
