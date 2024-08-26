from typing import TypedDict
import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("OPEN_WEATHER_MAP_APP_ID")
print(APP_ID)

Location = TypedDict("Location", {"lat": float, "lon": float})
LocationResponseData = TypedDict(
    "LocationResponseData", {"country": str, "name": str, "location": Location}
)
LocationResponse = LocationResponseData | Exception


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


WeatherResponseData = TypedDict(
    "WeatherResponseData",
    {
        "description": str,
        "temperature": float,
        "minTemperature": float,
        "maxTemperature": float,
        "humidity": int,
        "windSpeed": float,
    },
)

WeatherResponse = WeatherResponseData | Exception


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
    

# T = TypeVar("T")

# WeatherDataItem = TypedDict("WeatherDataItem", {"title": str, "unit": str, "value": T})

# WeatherData = TypedDict(
#     "WeatherData",
#     {
#         "description": WeatherDataItem[str],
#         "temperature": WeatherDataItem[float],
#         "minTemperature": WeatherDataItem[float],
#         "maxTemperature": WeatherDataItem[float],
#         "humidity": WeatherDataItem[int],
#         "windSpeed": WeatherDataItem[float],
#     },
# )

# UNITS = {
# "temperature": " Celsius",
# "minTemperature": " Celsius",
# "maxTemperature": " Celsius",
# "humidity": "%",
# "windSpeed": " m/s",
# }
    
# def parseWeatherResponse(weatherResponseData: WeatherResponseData) -> WeatherData:
#     parsedData = {key: {"title": camelCaseToTitleCase(key), "value": f"{value}{UNITS.get(key,"")}"} for key, value in weatherResponseData.items()}

#     return cast(WeatherData,parsedData)

# def camelCaseToTitleCase(camelCase: str) -> str:
#     return "".join(f" {ch}" if ch.upper() == ch else ch for ch in camelCase).capitalize()

