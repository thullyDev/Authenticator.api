from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.database import database
from app.database.cache.cache import Cache
import uuid

router: APIRouter = APIRouter(prefix="/auth")
cache: Cache = Cache()
response: ResponseHandler = ResponseHandler()

@router.post("/signup/")
def signup(username: str, email: str, password: str, confirm: str) -> JSONResponse:

     if len(password) < 10:
          return response.bad_request_response(data={ "message": "password should have length greater equal to 10" })

     if password != confirm:
          return response.bad_request_response(data={ "message": "password and confirm do not match" })

     data: Any = database.get_user(email=email)

     if data != None:
          return response.bad_request_response(data={ "message": "this user already exists" })

     ucode = uuid.uuid4() 
     _15minutes = 900
     cache_id = f"user_verify_code:{ucode}*15m"
     data = {
          "code": ucode,
          "email": data.email,
     }

     cache.hset(name=cache_id, expiry=_15minutes, data=data)

     return response.successful_response(data={ "message": "successfully signed up", "data": data })


def validator(*, request: Request, callnext):
     url_path = request.url.path
     temp = url_path.split("/")

     if "signup" in temp:
          return callnext(request) 

     return response.successful_response(data={ "message": "this is validator" })
