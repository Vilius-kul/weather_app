import fastapi

router = fastapi.APIRouter()
@router.get('/')
def index():
    return "Hello weather app!"