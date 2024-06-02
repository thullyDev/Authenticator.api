from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler


router: APIRouter = APIRouter(prefix="/auth")
response: ResponseHandler = ResponseHandler()

@router.get("/signup")
def signup() -> JSONResponse:
     return response.successful_response(data={ "message": "this is signup" })


def validator(*, request: Request, callnext):
     url_path = request.url.path
     temp = url_path.split("/")

     if "signup" in temp:
          return callnext(request) 

     return response.successful_response(data={ "message": "this is validator" })
