# -*- coding: utf-8 -*-
from weather import get_weather

city = input("Which city do you want to know the weather for?\n> ")
data = get_weather(city)

for day in data["consolidated_weather"]:
    desc = day["weather_state_name"]
    date = day["applicable_date"]
    temp = day["max_temp"]
    print(f"{date}: {desc} ({round(temp, 1)} °C)")