from typing import Optional

import requests

api_key: Optional[str] = None


def get_report(
    city: str, region: Optional[str]) -> dict:
    if region:
        q = f"{city},{region}"
    else:
        q = f"{city}"

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={q}&aqi=no"

    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()

    try:
        weather = {
            'temperature': data['current'].get('temp_c'),
            'condition': data['current']['condition'].get('text'),
            'icon': data['current']['condition'].get('icon'),
            'humidity': data['current'].get('humidity'),
            'windSpeed': data['current'].get('wind_kph'),
        }
    except KeyError as e:
        print(f"KeyError: {e}. The key does not exist in the response.")
        return {}

    return weather

