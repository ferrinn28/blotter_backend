import logging

from sqlmodel import Session, select
from typing import List, Tuple
from src.model import TPortfolio, TUser
from src.dto import PortfolioData
from .database import engine 


class TPortfolioRepo:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
    
    def get_portfolio_user(self, username:str) -> Tuple[List[PortfolioData], int, str]:
        """
        Queries all portfolio for specific username
        """
        with Session(engine) as session:
            
            # 1. SELECT statement on the TPortfolio model then 
            # join with TUser to filter portfolio based on username 
            statement = select(TPortfolio).join(TUser).where(TUser.username == username)

            # 2. Execute and fetch results
            results = session.exec(statement).all()

            data = [PortfolioData(name=entity.name,
                                  equity=entity.equity,
                                  currency_portfolio=entity.currency_portfolio.code,
                                  is_active=entity.is_active) for entity in results]
            

            status_code = 200
            msg = "OK"

            return data, status_code, msg
        