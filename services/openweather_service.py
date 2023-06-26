from fastapi import HTTPException
from typing import Optional
import requests

api_key: Optional[str] = None


def get_report(city: str, region: Optional[str]) -> dict:
    q = f"{city},{region}" if region else f"{city}"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={q}&aqi=no"
    resp = requests.get(url)

    try:
        resp.raise_for_status()
    except requests.HTTPError:
        if resp.status_code == 400:  # You might want to check the status code here
            data = resp.json()
            if data['error']['code'] == 1006:  # Check if error code is 1006
                raise HTTPException(status_code=400, detail="No matching location found.")
        raise HTTPException(status_code=500, detail="Something went wrong.")  # You can add a generic error message here

    data = resp.json()
    weather = {
        'temperature': data['current'].get('temp_c'),
        'condition': data['current']['condition'].get('text'),
        'icon': data['current']['condition'].get('icon'),
        'humidity': data['current'].get('humidity'),
        'windSpeed': data['current'].get('wind_kph'),
    }
    return weather


