from fastapi import FastAPI, Request
from typing import Any, Dict
from .routers import auth_router 
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler

app = FastAPI()
response: ResponseHandler = ResponseHandler()

def auth_middleware(request: Request, callnext):
    url_path = request.url.path
    temp = url_path.split("/")

    if "auth" in temp:
        return auth_router.validator(request=request, callnext=callnext) 

    return callnext(request)

app.middleware("http")(auth_middleware)

@app.exception_handler(Exception)
def unexpected_error_handler(request: Request, exc) -> JSONResponse:
    return response.crash_response(data={ "message": "Unexpected error occurred" })

@app.get("/")
def root() -> JSONResponse:
    return response.successful_response(data={ "message": "server is running... follow me on https://github.com/thullDev" })

app.include_router(auth_router.router)

