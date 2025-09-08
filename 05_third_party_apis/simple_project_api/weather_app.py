"""
Weather App using a free API.
Replace 'YOUR_API_KEY' with your real key from https://openweathermap.org/
"""

import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city="London"):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.ok:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description'].title()}")
        print(f"Temperature: {data['main']['temp']}°C")
    else:
        print("Error fetching weather:", response.status_code)

if __name__ == "__main__":
    get_weather("New York")
