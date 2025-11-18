import logging

from fastapi import APIRouter, Response, status

from src.dto import LoginRequest, LoginResponse
from src.service import LoginService


LoginController = APIRouter()

# OpenAPI Swagger Additional Responses
responses = {
    200: {"model": LoginResponse,
          "description": "Login Success",
          "content": {
                "application/json": {
                    "example": {"status": 200, "msg": "Login Success", "token": "PLACEHOLDER_JWT_TOKEN"}
                }}
        },

    404: {"model": LoginResponse,
          "description": "Login Failed",
          "content": {
                "application/json": {
                    "example": {"status": 404, "msg": "Wrong username or password", "token": "null"}
                }}
        }
}


@LoginController.post("/login", status_code=200, responses={**responses})
def login(user: LoginRequest, response: Response) -> LoginResponse:

    # Verify User Credential
    http_status, message, token = LoginService(user.username, user.password).verify()

    if http_status == 401:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return LoginResponse(
            status=http_status, 
            msg=message, 
            token=token)
    else:
        return LoginResponse(
            status=http_status, 
            msg=message, 
            token=token)