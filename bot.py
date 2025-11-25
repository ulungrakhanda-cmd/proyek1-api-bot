import requests
import os

API_KEY = os.getenv("OPENWEATHER_API")
CITY = "Jakarta"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    data = r.json()
    return f"Cuaca {CITY}: {data['main']['temp']}°C, {data['weather'][0]['description']}"

print(get_weather())
