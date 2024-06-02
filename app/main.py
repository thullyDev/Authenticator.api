from fastapi import FastAPI
from typing import Any, Dict
# from .routers import auth_router 
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler

app = FastAPI()
response: ResponseHandler = ResponseHandler()

async def custom_middleware(request, call_next):
    # if some_condition:
        # Return a custom response
    return JSONResponse({"message": "Custom response"}, status_code=200)

    # response = await call_next(request)
    # return response

# Register the middleware with the FastAPI app
app.middleware("http")(custom_middleware)

@app.exception_handler(Exception)
def unexpected_error_handler(request, exc) -> JSONResponse:
    return response.crash_response(data={ "message": "Unexpected error occurred" })

@app.get("/")
def root() -> JSONResponse:
    return response.successful_response(data={ "message": "server is running... follow me on https://github.com/thullDev" })

# app.include_router(auth_router.router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host=HOST, port=PORT)
