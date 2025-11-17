from sqlmodel import Session, select
from typing import Optional
from src.model import TUser
from .database import engine


class TUserRepo:

    def get_by_id(self, user_id: int) -> Optional[TUser]:
        """Reads a user by their ID."""
        with Session(engine) as session:
            user = session.get(TUser, user_id)
        
        return user

    def get_by_username(self, username: str) -> Optional[TUser]:
        """Reads a user by their unique username."""
        with Session(engine) as session:
            statement = select(TUser).where(TUser.username == username)
            user = session.exec(statement).first()

        return user