from typing import Optional

api_key: Optional[str] = None

def get_report(city: str, country: str, units: Optional[str]):
    q = f"{city},{country}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    print(url)