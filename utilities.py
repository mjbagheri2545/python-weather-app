import requests

def getWeather(searchText: str):
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.json())