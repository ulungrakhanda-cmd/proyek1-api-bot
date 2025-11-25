import os
import requests

CITY = "Jakarta"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()

    # cek kalau request gagal
    if res.status_code != 200 or "main" not in data:
        return f"Gagal ambil cuaca: {data.get('message', 'Unknown error')}"

    return f"Cuaca {CITY}: {data['main']['temp']}°C, {data['weather'][0]['description']}"

print(get_weather())
