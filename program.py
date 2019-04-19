# -*- coding: utf-8 -*-

import requests

BASE_URL = "https://www.metaweather.com"

def get_city_weoid(city):
    url = f"{BASE_URL}/api/location/search/?query={city}"
    response = requests.get(url)
    data = response.json()
    woeid = data[0]['woeid']
    return woeid

city = input("Which city do you want to know the weather for?\n> ")
url = f"{BASE_URL}/api/location/{get_city_weoid(city)}/"
response = requests.get(url)
data = response.json()

for day in data["consolidated_weather"]:
    desc = day["weather_state_name"]
    date = day["applicable_date"]
    temp = day["max_temp"]
    print(f"{date}: {desc} ({round(temp, 1)} °C)")