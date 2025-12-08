from sqlmodel import Field, SQLModel, Relationship
from .tcurrency import TCurrency
from .tuser import TUser
from datetime import datetime


class TPortfolio(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    
    user_id: int = Field(foreign_key="tuser.uid")
    name: str
    initial_equity: float
    equity: float
    currency_id: int = Field(foreign_key="tcurrency.id")
    dt_create: datetime
    dt_update: datetime
    is_active: int


    currency_portfolio: TCurrency = Relationship(
        back_populates="portfolio_currency",
        sa_relationship_kwargs={"foreign_keys": "TPortfolio.currency_id"}
    )

    user_portfolio: TUser = Relationship(
        back_populates="portfolio_user",
        sa_relationship_kwargs={"foreign_keys": "TPortfolio.user_id"}
    )
