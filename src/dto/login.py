from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str | None = None

class LoginResponse(BaseModel):
    status: int
    msg: str | None = None
    token: str | None = None