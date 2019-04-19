import requests

BASE_URL = "https://www.metaweather.com"

def get_city_weoid(city):
    url = f"{BASE_URL}/api/location/search/?query={city}"
    response = requests.get(url)
    data = response.json()
    woeid = data[0]['woeid']
    return woeid

def get_weather(city):
    url = f"{BASE_URL}/api/location/{get_city_weoid(city)}/"
    response = requests.get(url)
    data = response.json()
    return data
