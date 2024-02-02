# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:34:31 2024

@author: Parshv
"""

import requests
import os
from datetime import datetime

def get_weather_data(location, api_key):
    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    api_link = requests.get(complete_api_link)

    if api_link.status_code == 200:
        return api_link.json()
    else:
        return None

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    user_api = os.environ.get('current_weather_data')
    if not user_api:
        print("API key not found. Please set the 'current_weather_data' environment variable.")
        return

    location = input("Enter the city name: ").capitalize()

    api_data = get_weather_data(location, user_api)

    if api_data:
        temp_city = convert_kelvin_to_celsius(api_data['main']['temp'])
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("-------------------------------------------------------------")
        print("Weather Stats for - {}  || {}".format(location, date_time))
        print("-------------------------------------------------------------")
        print("Current temperature is: {:.2f} deg C".format(temp_city))
        print("Current weather desc  :", weather_desc)
        print("Current Humidity      :", hmdt, '%')
        print("Current wind speed    :", wind_spd, 'kmph')
    else:
        print(f"Unable to fetch weather data for {location}.")

if __name__ == "__main__":
    main()
