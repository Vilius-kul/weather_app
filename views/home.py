import fastapi

router = fastapi.APIRouter()


@router.get("/")
def index() -> str:
    return "Hello weather app!"
