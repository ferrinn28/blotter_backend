from fastapi import APIRouter, Response, status
from src.service import CurrencyPairService
from src.dto import CurrencyPairResponse
from src.openapi_config import response_currencypair_controller_get


CurrencyPairController = APIRouter(tags=["Currency Pairs"])


@CurrencyPairController.get("/currencypair/{currency_pair}", status_code=200, responses={**response_currencypair_controller_get})
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
                msg="Invalid currency pair code format. Expected 6 characters (e.g., 'usdidr')",
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