import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY_ID = 1254360
url = f'https://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}'
response = requests.get(url)
weather_data = response.json()

print("🌤️ Weather for Tirupati")
print(f"🌡️ Temperature: {round(weather_data['main']['temp'] - 273.15,2)}\u00b0C (Feels like {round(weather_data['main']['feels_like'] - 273.15,2)}\u00b0C)")
print(f'☁️ Condition: {weather_data["weather"][0]["main"]}')
print(f'💧 Humidity: {weather_data["main"]["humidity"]}%')
print(f'💨 Wind: {round(weather_data["wind"]["speed"] * 3.6,2)}km/h')
print(f'🔽 Pressure: {weather_data["main"]["pressure"]}hPa')
print(f'👁️ Visibility: {weather_data["visibility"]}m')

sunrise = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime("%I:%M %p")
sunset = datetime.datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%I:%M %p')

print(f'🌅 Sunrise: {sunrise}')
print(f'🌇 Sunset: {sunset}')
