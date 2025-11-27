import logging

from sqlmodel import Session, select
from typing import List, Tuple
from src.model import TCurrencyPair, TCurrency
from src.dto import CurrencyPairData
from .database import engine 


class TCurrencyPairRepo:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
    
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

                self.log.warning(f"Currency pair {currency_pair} is not found in DB")

                return data, status_code, msg
            
    def post_currency_pair(self, base_currency:str, quote_currency:str) -> Tuple[List[CurrencyPairData], int, str]:
        """
        Adding New Currency Pair into DB
        """
        with Session(engine) as session:
            # 1. SELECT statement on the TCurrency WHERE code is equal with base_currency and quote currency
            statement_base_currency = select(TCurrency).where(TCurrency.code == base_currency)

            statement_quote_currency = select(TCurrency).where(TCurrency.code == quote_currency)

            # 2. Execute and fetch results
            results_base_currency = session.exec(statement_base_currency).first()
            results_quote_currency = session.exec(statement_quote_currency).first()


            # 3. Add TCurrencyPair
            new_currency_pair = TCurrencyPair(
                currency_pair=f"{base_currency}/{quote_currency}",
                base_currency=results_base_currency,
                quote_currency=results_quote_currency

            )

            session.add(new_currency_pair)
            session.commit()

            self.log.info(f"Currency pair {base_currency}/{quote_currency} is already added into DB")

            session.refresh(new_currency_pair)
            data = [CurrencyPairData(name=new_currency_pair.currency_pair,
                                        base_currency=new_currency_pair.base_currency.code,
                                        base_desc=new_currency_pair.base_currency.description,
                                        quote_currency=new_currency_pair.quote_currency.code,
                                        quote_desc=new_currency_pair.quote_currency.description)]
            status_code = 201
            msg = "ADDED"

            return data, status_code, msg
    
    def delete_currency_pair(self, base_currency:str, quote_currency:str) -> Tuple[List[CurrencyPairData], int, str]:
        """
        Delete Specific Currency Pair into DB
        """
        with Session(engine) as session:
            # 1. SELECT statement on the TCurrency WHERE code is equal with currency pair name
            currency_pair = f"{base_currency}/{quote_currency}"
            statement = select(TCurrencyPair).where(TCurrencyPair.currency_pair == currency_pair)

            result_currency_pair = session.exec(statement).one()

            # Save deleted data first into variable
            data = [CurrencyPairData(name=result_currency_pair.currency_pair,
                                        base_currency=result_currency_pair.base_currency.code,
                                        base_desc=result_currency_pair.base_currency.description,
                                        quote_currency=result_currency_pair.quote_currency.code,
                                        quote_desc=result_currency_pair.quote_currency.description)]

            # 2. Delete TCurrencyPair
            session.delete(result_currency_pair)
            session.commit()
            

            self.log.info(f"Delete Currency pair {base_currency}/{quote_currency} is already success")

            
            status_code = 200
            msg = "DELETED"

            return data, status_code, msg