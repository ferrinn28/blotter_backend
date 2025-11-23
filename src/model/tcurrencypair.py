from sqlmodel import Field, SQLModel, Relationship
from .tcurrency import TCurrency


class TCurrencyPair(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    currency_pair: str 
    
    base_id: int = Field(foreign_key="tcurrency.id")
    quote_id: int = Field(foreign_key="tcurrency.id")
    

    base_currency: TCurrency = Relationship(
        back_populates="base_pairs",
        sa_relationship_kwargs={"foreign_keys": "TCurrencyPair.base_id"}
    )

    quote_currency: TCurrency = Relationship(
        back_populates="quote_pairs",
        sa_relationship_kwargs={"foreign_keys": "TCurrencyPair.quote_id"}
    )
