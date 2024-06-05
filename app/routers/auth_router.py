from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.database import database

router: APIRouter = APIRouter(prefix="/auth")
response: ResponseHandler = ResponseHandler()

@router.post("/signup/")
def signup(username: str, email: str, password: str, confirm: str) -> JSONResponse:
     data = database.get_user(email=email)

     if len(password) < 10:
          return response.bad_request_response(data={ "message": "password should have length greater equal to 10" })

     if password != confirm:
          return response.bad_request_response(data={ "message": "password and confirm do not match" })

     return response.successful_response(data={ "message": "successfully signed up" })


def validator(*, request: Request, callnext):
     url_path = request.url.path
     temp = url_path.split("/")

     if "signup" in temp:
          return callnext(request) 

     return response.successful_response(data={ "message": "this is validator" })
