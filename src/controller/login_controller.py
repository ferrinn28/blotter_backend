from fastapi import APIRouter, Response, status

from src.dto import LoginRequest, LoginResponse
from src.service import LoginService
from src.openapi_config import response_login_controller


LoginController = APIRouter(tags=["Login"])


@LoginController.post("/login", status_code=200, responses={**response_login_controller})
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