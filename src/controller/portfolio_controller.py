from fastapi import APIRouter
from src.service import PortfolioService
from src.dto import PortfolioResponse
from src.openapi_config import response_portfolio_controller_get


PortfolioController = APIRouter(prefix="/portfolio", tags=["Portfolio"])

@PortfolioController.get("/{user_name}", status_code=200, responses={**response_portfolio_controller_get})
def portfolio(user_name:str) -> PortfolioResponse:
    
    data, status_code, msg, owner_username = PortfolioService().search_portfolio_by_username(user_name)
    
    return PortfolioResponse(
        status=status_code,
        msg=msg,
        username=owner_username,
        portfolios=data
    )