from fastapi import APIRouter, HTTPException, Response, status
from src.service import CurrencyPairService
from src.dto import CurrencyPairResponse


CurrencyPairController = APIRouter(tags=["Currency Pairs"])

# OpenAPI Swagger Additional Responses
responses = {
    200: {"model": CurrencyPairResponse,
          "description": "Success Query Registered Currency Pairs",
          "content": {
                "application/json": {
                    "example": {"status": 200, 
                                "msg": "OK", 
                                "currency_pairs": [
                                                    {
                                                        "name": "USD/IDR",
                                                        "base_currency": "USD",
                                                        "base_desc": "United States Dollar",
                                                        "quote_currency": "IDR",
                                                        "quote_desc": "Indonesia Rupiah"
                                                    },
                                                    {
                                                        "name": "AUD/USD",
                                                        "base_currency": "AUD",
                                                        "base_desc": "Australia Dollar",
                                                        "quote_currency": "USD",
                                                        "quote_desc": "United States Dollar"
                                                    }]}
                }}
        },

    400: {"model": CurrencyPairResponse,
          "description": "Wrong Currency Pair Format",
          "content": {
                "application/json": {
                    "example": {"status": 400, 
                                "msg": "Invalid currency pair code format. Expected 6 characters (e.g., 'usdidr').", 
                                "currency_pairs": "null"}
                }}
        },

    404: {"model": CurrencyPairResponse,
          "description": "Currency Pair Not Found",
          "content": {
                "application/json": {
                    "example": {"status": 404, "msg": "NOT FOUND", "currency_pairs": "null"}
                }}
        }
}


@CurrencyPairController.get("/currencypair/{currency_pair}", status_code=200, responses={**responses})
def currencypair(currency_pair:str, response: Response) -> CurrencyPairResponse :
    
    if currency_pair == "all":
        data, status_code, msg = CurrencyPairService().all()

    else:
        # Based on ISO 4217 base and quote currency have 3 letters
        # example: EURUSD, GBPUSD, etc
        if len(currency_pair) != 6:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return CurrencyPairResponse(
                status=400,
                msg="Invalid currency pair code format. Expected 6 characters (e.g., 'usdidr').",
                currency_pairs=None
            )
            

        # Extract Base and Quote Currency
        base_code = currency_pair[:3].upper()
        quote_code = currency_pair[3:].upper()
    
        # The final, standard currency pair string
        standard_pair_code = f"{base_code}/{quote_code}"
        response.status_code = status.HTTP_404_NOT_FOUND
        data, status_code, msg = CurrencyPairService().search(standard_pair_code)

    
    return CurrencyPairResponse(status=status_code, msg=msg,currency_pairs=data)