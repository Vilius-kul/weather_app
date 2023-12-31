import fastapi
from fastapi import Depends

from models.location import Location
from services import openweather_service

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(loc: Location = Depends()) -> dict:
    return openweather_service.get_report(loc.city, loc.region)
