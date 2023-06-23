import fastapi
import uvicorn

from views import home
from api import weather_api

api = fastapi.FastAPI()



def configure():
    configure_routing()

def configure_routing():
    api.include_router(home.router)
    api.include_router(weather_api.router)

if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
     configure()