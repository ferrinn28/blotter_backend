import logging

from src.repository import TPortfolioRepo, TUserRepo
from src.dto import PortfolioData
from typing import Tuple, List


class PortfolioService:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def search_portfolio_by_username(self, username:str) -> Tuple[List[PortfolioData], int, str, str] :
        self.log.info(f"Quering All Portfolio username {username}")

        # Check user_name is exist in DB
        user_obj = TUserRepo().get_by_username(username)

        if user_obj:
            data, status_code, msg = TPortfolioRepo().get_portfolio_user(username)
            owner_username = user_obj.username

            return data, status_code, msg, owner_username
        else:
            self.log.warning(f"username {username} is not exist in DB")

            data = None
            status_code = 404
            msg = f"username {username} is not exist"
            owner_username = None

            return data, status_code, msg, owner_username
