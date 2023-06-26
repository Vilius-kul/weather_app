import json
from pathlib import Path

import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from api import weather_api
from custom_exceptions import SettingsFileNotFoundError
from services import openweather_service

api = fastapi.FastAPI()

origins = [
    "*"
]  # allowing all origins can expose your application to potential security risks, such as cross-site request forgery (CSRF) attacks

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def configure() -> None:
    configure_routing()
    configure_api_keys()


def configure_routing() -> None:
    api.include_router(weather_api.router)


def configure_api_keys() -> None:
    file = Path("settings.json").absolute()
    if not file.exists():
        print(
            f"WARNING: {file} file not found, you cannot continue, please see settings_template.json"
        )
        raise SettingsFileNotFoundError(
            "settings.json file not found, you cannot continue, please see settings_template.json"
        )

    with open(file) as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get("api_key")


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()
