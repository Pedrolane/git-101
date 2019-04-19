# -*- coding: utf-8 -*-

import requests

BASE_URL = "https://www.metaweather.com"

city = input("City?\n> ")

url = f"{BASE_URL}/api/location/search/?query={city}"
response = requests.get(url)
data = response.json()
woeid = data[0]['woeid']

url = f"{BASE_URL}/api/location/{woeid}/"
response = requests.get(url)
data = response.json()
print(data)

for day in data["consolidated_weather"]:
    desc = day["weather_state_name"]
    date = day["applicable_date"]
    temp = day["max_temp"]
    print(f"{date}: {desc} ({temp} °C)")