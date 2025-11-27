import logging

from src.repository import TCurrencyPairRepo
from src.model import TCurrencyPair
from typing import Tuple, List


class CurrencyPairService:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def all(self) -> Tuple[List[TCurrencyPair], int, str]:
        self.log.info("Quering All Currency Pair")
        data, status_code, msg = TCurrencyPairRepo().get_all_pairs_with_names()

        return data, status_code, msg
    
    def search(self, currency_pair:str) -> Tuple[List[TCurrencyPair], int, str]:
        self.log.info(f"Quering {currency_pair} Data")
        data, status_code, msg = TCurrencyPairRepo().get_specific_pairs_with_names(currency_pair)

        return data, status_code, msg
    
    def add(self, base_currency:str, quote_currency:str) -> Tuple[List[TCurrencyPair], int, str]:
        currency_pair = f"{base_currency}/{quote_currency}"
        self.log.info(f"Registering {currency_pair} into DB")

        # Checking Currency Pair is already exist or not
        data, _, _ = TCurrencyPairRepo().get_specific_pairs_with_names(currency_pair)

        if data == None:
            output, status_code, msg = TCurrencyPairRepo().post_currency_pair(base_currency, quote_currency)
            self.log.info(f"Currency Pair {currency_pair} success added")
            return output, status_code, msg
        
        else:
            self.log.warning(f"Currency Pair {currency_pair} already exist in DB")
            status_code = 200
            msg = "Already Exist in DB"
            return data, status_code, msg
        
    def delete(self, base_currency:str, quote_currency:str) -> Tuple[List[TCurrencyPair], int, str]:
        currency_pair = f"{base_currency}/{quote_currency}"
        self.log.info(f"Deleting {currency_pair} into DB")

        # Checking Currency Pair is already exist or not
        data, _, _ = TCurrencyPairRepo().get_specific_pairs_with_names(currency_pair)

        if data != None:
            output, status_code, msg = TCurrencyPairRepo().delete_currency_pair(base_currency, quote_currency)
            self.log.info(f"Currency Pair {currency_pair} success deleted")
            return output, status_code, msg
        
        else:
            self.log.warning(f"Can't Delete Currency Pair {currency_pair} becasue Can't be found in DB")
            status_code = 400
            msg = "NOT FOUND"
            return data, status_code, msg

