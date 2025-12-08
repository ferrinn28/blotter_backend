from src.dto import PortfolioResponse


# OpenAPI Swagger Additional Responses
response_portfolio_controller_get = {
    200: {"model": PortfolioResponse,
          "description": "Success Query All Portfolio based on Username",
          "content": {
                "application/json": {
                    "example": {"status": 200, 
                                "msg": "OK",
                                "username": "admin",
                                "portfolios": [
                                                    {
                                                        "name": "Portfolio 1",
                                                        "equity": 30,
                                                        "currency_portfolio": "USD",
                                                        "is_active": 1,
                                                    },
                                                    {
                                                        "name": "Portfolio 2",
                                                        "equity": 50,
                                                        "currency_portfolio": "USD",
                                                        "is_active": 0,
                                                    }]}
                }}
        },

    404: {"model": PortfolioResponse,
          "description": "Username has not found in DB",
          "content": {
                "application/json": {
                    "example": {"status": 404, 
                                "msg": "username admin1 is not exist",
                                "username": "null",
                                "portfolios": "null"}
                }}
        }
}