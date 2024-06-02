from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.resources.errors import CRASH

router: APIRouter = APIRouter(prefix="/auth")
response: ResponseHandler = ResponseHandler()


@router.get("/signup")
async def signup() -> JSONResponse:
     return response.successful_response()