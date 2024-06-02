# from fastapi import APIRouter, Depends
# from fastapi.responses import JSONResponse
# from app.handlers.response_handler import ResponseHandler
# from app.resources.errors import CRASH

# router: APIRouter = APIRouter(prefix="/auth")
# response: ResponseHandler = ResponseHandler()


# Custom middleware function
# async def custom_middleware(request, call_next):
    # Check if a specific condition is met
    # if some_condition:
        # Return a custom response
        # return response.successful_response({"message": "Custom response"})

    # If the condition is not met, continue with the request
    # response = await call_next(request)
    # return response

# Register the middleware with the FastAPI app
# router.middleware("http")(custom_middleware)

# def verify_request():
#      token = None
     
#      if not token:
#           return {"status_code": 401, "detail": "Invalid token"}


# @router.get("/signup")
# def signup(token: str = Depends(verify_request)) -> JSONResponse:
#      return response.successful_response()