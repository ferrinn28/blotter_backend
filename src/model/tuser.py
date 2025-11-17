from sqlmodel import Field, SQLModel


class TUser(SQLModel, table=True):
    uid: int = Field(primary_key=True)
    name: str
    username: str
    password: str
    last_login: str