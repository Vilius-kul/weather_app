import fastapi
import uvicorn
import json

from pathlib import Path

from custom_exceptions import SettingsFileNotFoundError
from services import openweather_service
from views import home
from api import weather_api

api = fastapi.FastAPI()



def configure():
    configure_routing()
    configure_api_keys()

def configure_routing():
    api.include_router(home.router)
    api.include_router(weather_api.router)



def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise SettingsFileNotFoundError("settings.json file not found, you cannot continue, please see settings_template.json")

    with open(file) as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
     configure()