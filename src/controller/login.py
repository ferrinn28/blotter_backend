import logging

from fastapi import APIRouter

from src.dto import LoginRequest, LoginResponse
import src.service as service

Login = APIRouter()

@Login.post("/login")
def login(user: LoginRequest) -> LoginResponse:
    logging.info("Login")

    service.Login(user.username, user.password).verify()
    
    return LoginResponse(
        msg="Login successful",
        token="token", 
        status="OK"
    )