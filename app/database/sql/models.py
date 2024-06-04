from sqlmodel import Field, SQLModel

class user(SQLModel, table=True):
    id: int 
    username: str
    email: str
    token: str
