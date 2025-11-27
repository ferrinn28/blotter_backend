from fastapi import APIRouter, Response, status
from src.service import CurrencyPairService
from src.dto import CurrencyPairResponse, CurrencyPairRequest
from src.openapi_config import response_currencypair_controller_get, response_currencypair_controller_post, response_currencypair_controller_delete


CurrencyPairController = APIRouter(tags=["Currency Pairs"])
msg_400 = "Invalid currency pair code format. Expected 6 characters (e.g., 'usdidr')"


@CurrencyPairController.get("/currencypair/{currency_pair}", status_code=200, responses={**response_currencypair_controller_get})
def query_currency_pair(currency_pair:str, response: Response) -> CurrencyPairResponse :
    
    if currency_pair == "all":
        data, status_code, msg = CurrencyPairService().all()

    else:
        # Based on ISO 4217 base and quote currency have 3 letters
        # example: EURUSD, GBPUSD, etc
        if len(currency_pair) != 6:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return CurrencyPairResponse(
                status=400,
                msg=msg_400,
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


@CurrencyPairController.post("/currencypair", responses={**response_currencypair_controller_post})
def add_currency_pair(data: CurrencyPairRequest, response: Response) -> CurrencyPairResponse:

    # Based on ISO 4217 base and quote currency have 3 letters
    # example: EURUSD, GBPUSD, etc
    if len(data.currency_pair) != 6:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return CurrencyPairResponse(
                status=400,
                msg=msg_400,
                currency_pairs=None
            )
    
    # Extract Base and Quote Currency
    base_code = data.currency_pair[:3].upper()
    quote_code = data.currency_pair[3:].upper()

    data, status_code, msg = CurrencyPairService().add(base_code, quote_code)
    if msg == "ADDED":
         response.status_code = status.HTTP_201_CREATED
    else:
         response.status_code = status.HTTP_200_OK
         

    return CurrencyPairResponse(status=status_code, msg=msg, currency_pairs=data)


@CurrencyPairController.delete("/currencypair/{currency_pair}", status_code=200, responses={**response_currencypair_controller_delete})
def delete_currency_pair(currency_pair:str, response: Response) -> CurrencyPairResponse:

    # Based on ISO 4217 base and quote currency have 3 letters
    # example: EURUSD, GBPUSD, etc
    if len(currency_pair) != 6:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return CurrencyPairResponse(
                status=400,
                msg=msg_400,
                currency_pairs=None
            )
    
    # Extract Base and Quote Currency
    base_code = currency_pair[:3].upper()
    quote_code = currency_pair[3:].upper()

    data, status_code, msg = CurrencyPairService().delete(base_code, quote_code)
    if msg == "DELETED":
         response.status_code = status.HTTP_200_OK
    else:
         response.status_code = status.HTTP_404_NOT_FOUND
         

    return CurrencyPairResponse(status=status_code, msg=msg, currency_pairs=data)