from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.database import database
from app.database.cache import cache 
import uuid
from app.resources.config import EMAIL, EMAIL_PASS, SITE_NAME, VERIFY_ENDPOINT
import yagmail

router: APIRouter = APIRouter(prefix="/auth")
response: ResponseHandler = ResponseHandler()

@router.post("/signup/")
def signup(request: Request, username: str, email: str, password: str, confirm: str) -> JSONResponse:
     if len(password) < 10:
          return response.bad_request_response(data={ "message": "password should have a length greater equal to 10" })

     if password != confirm:
          return response.bad_request_response(data={ "message": "password and confirm do not match" })

     if not isEmailValidate(email): 
          return response.bad_request_response(data={ "message": "email is invalid" })

     data = database.get_user(email=email)

     if data != None:
          return response.bad_request_response(data={ "message": "this user already exists" })


     ucode = uuid.uuid4() 
     verify_link =  create_verification_link(code=ucode, request=request)

     if not send_verification(email, verify_link=verify_link):
          return response.crash_response(data={ "message": "Failed to send the verification email, please try again later" })

     _15minutes = 900
     cache_id = f"user_verify_code:{ucode}*15m"
     data = {
          "code": ucode,
          "email": email,
          "password": password,
          "username": username,
     }

     cache.hset(name=cache_id, expiry=_15minutes, data=data)
     del data["code"]
     return response.successful_response(data={ "message": "verify now", "data": data })


def validator(*, request: Request, callnext) -> JSONResponse:
     url_path = request.url.path
     temp = url_path.split("/")

     if "signup" in temp:
          return callnext(request) 

     return response.successful_response(data={ "message": "this is validator" })

def send_email(*, subject: str, body: str, to_email: str):
    yag = yagmail.SMTP(EMAIL, EMAIL_PASS)

    response = yag.send(
        to=to_email,
        subject=subject,
        contents=body
    )

    yag.close()

    if response == False:
     return False

     return True

import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isEmailValidate(email: str) -> bool:
     if re.fullmatch(regex, email):
          return False
     else:
          return True

def send_verification(email: str, verify_link: str):
   body = f"Verification for {SITE_NAME} please follow the link {verify_link} to verify"
   subject = f"{SITE_NAME} verification"

   return send_email(subject=subject, body=body, to_email=email)

def create_verification_link(*, request: Request, code: uuid.UUID):
     endpoint = ""
     if VERIFY_ENDPOINT != "null":
          endpoint = VERIFY_ENDPOINT
     else:
          # if the verify endpoint is not gaven in the .env, we'll user the authenticator's verify endpoint
          endpoint = request.url._url.replace("/auth/signup/", "").replace("//", "/") 

     verify_link =  f"{endpoint}/verify={code}"

     return verify_link