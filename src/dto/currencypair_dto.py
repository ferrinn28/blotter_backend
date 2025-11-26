from pydantic import BaseModel
from typing import List


class CurrencyPairData(BaseModel):
    name: str | None
    base_currency: str | None
    base_desc: str | None
    quote_currency: str | None
    quote_desc: str | None
    
class CurrencyPairResponse(BaseModel):
    status: int
    msg: str
    currency_pairs: List[CurrencyPairData] | None

class CurrencyPairRequest(BaseModel):
    currency_pair: str
