from sqlmodel import Session, select
from typing import List, Tuple
from src.model import TCurrencyPair
from src.dto import CurrencyPairData
from .database import engine 


class TCurrencyPairRepo:
    
    def get_all_pairs_with_names(self) -> Tuple[List[CurrencyPairData], int, str]:
        """
        Queries all currency pairs and joins TCurrency twice to fetch 
        the full Base and Quote currency details.
        """
        with Session(engine) as session:
            
            # 1. SELECT statement on the TCurrencyPair model
            statement = select(TCurrencyPair)

            # 2. Execute and fetch results
            results = session.exec(statement).all()

            data = [CurrencyPairData(name=entity.currency_pair,
                                     base_currency=entity.base_currency.code,
                                     base_desc=entity.base_currency.description,
                                     quote_currency=entity.quote_currency.code,
                                     quote_desc=entity.quote_currency.description) for entity in results]

            status_code = 200
            msg = "OK"

            return data, status_code, msg
        
    def get_specific_pairs_with_names(self, currency_pair:str) -> Tuple[List[CurrencyPairData], int, str]: 
        """
        Queries specific currency pairs and joins TCurrency twice to fetch 
        the full Base and Quote currency details.
        """
        with Session(engine) as session:
            
            # 1. SELECT statement on the TCurrencyPair model
            statement = select(TCurrencyPair).where(TCurrencyPair.currency_pair==currency_pair)

            # 2. Execute and fetch results
            results = session.exec(statement).first()

            if results:

                data = [CurrencyPairData(name=results.currency_pair,
                                        base_currency=results.base_currency.code,
                                        base_desc=results.base_currency.description,
                                        quote_currency=results.quote_currency.code,
                                        quote_desc=results.quote_currency.description)]
                
                status_code = 200
                msg = "OK"

                return data, status_code, msg
            
            else:
                data = None
                status_code = 404
                msg = "NOT FOUND"

                return data, status_code, msg