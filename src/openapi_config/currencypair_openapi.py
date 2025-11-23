from src.dto import CurrencyPairResponse


# OpenAPI Swagger Additional Responses
response_currencypair_controller_get = {
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
                                "msg": "Invalid currency pair code format. Expected 6 characters (e.g., 'usdidr')", 
                                "currency_pairs": "null"}
                }}
        },

    404: {"model": CurrencyPairResponse,
          "description": "Currency Pair Not Found",
          "content": {
                "application/json": {
                    "example": {"status": 404, 
                                "msg": "NOT FOUND", 
                                "currency_pairs": "null"}
                }}
        }
}