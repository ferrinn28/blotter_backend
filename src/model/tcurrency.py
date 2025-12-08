from sqlmodel import Field, SQLModel, Relationship
from typing import List


class TCurrency(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    code: str 
    description: str


    base_pairs: List["TCurrencyPair"] = Relationship(
        back_populates="base_currency",
        sa_relationship_kwargs={"foreign_keys": "TCurrencyPair.base_id"}
    )

    quote_pairs: List["TCurrencyPair"] = Relationship(
        back_populates="quote_currency",
        sa_relationship_kwargs={"foreign_keys": "TCurrencyPair.quote_id"}
    )

    portfolio_currency: List["TPortfolio"] = Relationship(
        back_populates="currency_portfolio",
        sa_relationship_kwargs={"foreign_keys": "TPortfolio.currency_id"}
    )