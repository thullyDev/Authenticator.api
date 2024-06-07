from fastapi import FastAPI, Request
from .routers import auth_router 
from fastapi.responses import JSONResponse
from app.handlers import response_handler as response

app = FastAPI()

@app.exception_handler(Exception)
def unexpected_error_handler() -> JSONResponse:
    return response.crash_response(data={ "message": "Unexpected error occurred" })

@app.get("/")
def root() -> JSONResponse:
    return response.successful_response(data={ "message": f"server is running... follow me on https://github.com/thullDev" })

app.include_router(auth_router.router)

