from typing import TypedDict
import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("OPEN_WEATHER_MAP_APP_ID")
print(APP_ID)

Location = TypedDict("Location", {"lat": float, "lon": float})
LocationData = TypedDict(
    "LocationData", {"country": str, "name": str, "location": Location}
)
LocationResponse = LocationData | Exception


def getLocation(cityName: str) -> LocationResponse:
    try:
        response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={cityName}&appid={APP_ID}"
        )
        location = response.json()[0]
        return {
            "country": location["country"],
            "name": location["name"],
            "location": {"lat": location["lat"], "lon": location["lon"]},
        }
    except Exception as e:
        return e


WeatherData = TypedDict(
    "WeatherData",
    {
        "description": str,
        "temperature": float,
        "minTemperature": float,
        "maxTemperature": float,
        "humidity": int,
        "windSpeed": float,
    },
)

WeatherResponse = WeatherData | Exception


def getWeather(location: Location) -> WeatherResponse:
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={location["lat"]}&lon={location['lon']}&appid={APP_ID}&units=metric"
        )

        weatherData = response.json()
        mainWeatherData = weatherData["main"]

        return {
            "description": weatherData["weather"][0]["description"],
            "temperature": mainWeatherData["temp"],
            "minTemperature": mainWeatherData["temp_min"],
            "maxTemperature": mainWeatherData["temp_max"],
            "humidity": mainWeatherData["humidity"],
            "windSpeed": weatherData["wind"]["speed"],
        }
    except Exception as e:
        return e

