from sqlmodel import Field, SQLModel, Relationship
from typing import List


class TUser(SQLModel, table=True):
    uid: int = Field(primary_key=True)
    name: str
    username: str
    password: str
    last_login: str


    portfolio_user: List["TPortfolio"] = Relationship(
        back_populates="user_portfolio",
        sa_relationship_kwargs={"foreign_keys": "TPortfolio.user_id"}
    )