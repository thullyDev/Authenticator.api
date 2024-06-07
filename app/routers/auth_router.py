from typing import Any, Optional, Dict
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.database.models import SetUser
from app.handlers import response_handler as response
from app.database import database
from app.database.cache import cache 
from app.resources.config import EMAIL, EMAIL_PASS, SITE_NAME, VERIFY_ENDPOINT
import uuid
import re
import hashlib
import yagmail

router: APIRouter = APIRouter(prefix="/auth")

@router.post("/signup/")
def signup(request: Request, username: str, email: str, password: str, confirm: str) -> JSONResponse:
     if len(password) < 10:
          return response.bad_request_response(data={ "message": "password should have a length greater equal to 10" })

     if password != confirm:
          return response.bad_request_response(data={ "message": "password and confirm do not match" })

     if not isEmailValidate(email): 
          return response.bad_request_response(data={ "message": "email is invalid" })

     user = database.get_user(key="email", entity=email)

     if user != None:
          return response.bad_request_response(data={ "message": "this user already exists" })


     ucode = str(uuid.uuid4() )
     verify_link = create_verification_link(code=ucode, request=request, _type="signup")

     if not send_verification(email, verify_link=verify_link):
          return response.crash_response(data={ "message": "Failed to send the verification email, please try again later" })

     _15minutes = 900
     cache_id = f"user_verify_code:{ucode}*15m"
     data = {
          "email": email,
          "password": password,
          "username": username,
     }

     cache.hset(name=cache_id, expiry=_15minutes, data=data)

     return response.successful_response(data={ "message": "verify now", "data": data })

@router.get("/verify/{_type}/{code}")
def verify(_type: str, code: str):
     cache_id = f"user_verify_code:{code}*15m"
     data: Any = cache.hget(name=cache_id)

     if data == None:
          return response.bad_request_response(data={ "message": "invalid code" })

     token = generate_unique_token()
     user = (data["username"], data["email"], data["password"])
     database.set_user(SetUser(user=user))
     cache.delete(name=cache_id)
     
     return response.successful_response(data={ "message": "successfully signed up", "data": data })

@router.post("/login/")
def login(email: str, password: str) -> JSONResponse:
     user = database.get_user(key="email", entity=email)

     if not user:
          return response.bad_request_response(data={ "message": "this email is not registered" })
     
     token = generate_unique_token()
     database.update_user(key="email", entity=email)

     data = {
          "email": user.email,
          "username": user.username,
          "token": token,
          "profile_image_url": user.profile_image_url,
     }
     return response.successful_response(data={ "message": "successfully logged in", "data": data })

# def validator(*, request: Request, callnext) -> JSONResponse:
#      url_path = request.url.path
#      temp = url_path.split("/")

#      if "signup" in temp:
#           return callnext(request) 

#      return response.successful_response(data={ "message": "this is validator" })

def send_email(*, subject: str, body: str, to_email: str) -> bool:
     yag = yagmail.SMTP(user=EMAIL, password=EMAIL_PASS)
     response = yag.send(
          to=to_email,
          subject=subject,
          contents=body
     )
     yag.close()
     if response == False:
          return False

     return True

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isEmailValidate(email: str) -> bool:
     if re.fullmatch(regex, email):
          return True
     else:
          return False

def send_verification(email: str, verify_link: str) -> bool:
     print(verify_link)
     return True

     body = f"Verification for {SITE_NAME} please follow the link {verify_link} to verify"
     subject = f"{SITE_NAME} verification"
     return send_email(subject=subject, body=body, to_email=email)

def create_verification_link(*, request: Any, code: str, _type: str):
     endpoint = VERIFY_ENDPOINT

     if VERIFY_ENDPOINT == "null":
          # if the verify endpoint is not gaven in the .env, we'll user the authenticator's verify endpoint
          url = request.url._url
          endpoint = url.replace("//", "**").split("/")[0].replace("**", "//") # extracting the host for the server

     verify_link =  f"{endpoint}/auth/verify/{_type}/{code}"

     return verify_link

def generate_unique_token(length: int = 250):
    random_uuid = uuid.uuid4()
    uuid_bytes = random_uuid.bytes
    hashed_token = hashlib.sha256(uuid_bytes).hexdigest()
    while len(hashed_token) < length:
        hashed_token += hashlib.sha256(hashed_token.encode()).hexdigest()

    hashed_token = hashed_token[:length]

    return hashed_token