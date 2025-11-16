from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str | None = None

class LoginResponse(BaseModel):
    status: str
    msg: str | None = None
    token: str | None = None