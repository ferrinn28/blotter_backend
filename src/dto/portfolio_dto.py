from pydantic import BaseModel
from typing import List


class PortfolioData(BaseModel):
    name: str | None
    equity: float | None
    currency_portfolio: str | None
    is_active: int | None
    
class PortfolioResponse(BaseModel):
    status: int
    msg: str
    username: str | None
    portfolios: List[PortfolioData] | None