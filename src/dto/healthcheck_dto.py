from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str
    msg: str | None = None