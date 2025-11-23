import logging

from src.repository import TCurrencyPairRepo
from src.model import TCurrencyPair
from typing import Tuple, List


class CurrencyPairService:
    def all(self) -> Tuple[List[TCurrencyPair], int, str]:
        logging.info("Quering All Currency Pair")
        data, status_code, msg = TCurrencyPairRepo().get_all_pairs_with_names()

        return data, status_code, msg
    
    def search(self, currency_pair:str) -> Tuple[List[TCurrencyPair], int, str]:
        logging.info(f"Quering {currency_pair} Data")
        data, status_code, msg = TCurrencyPairRepo().get_specific_pairs_with_names(currency_pair)

        return data, status_code, msg
