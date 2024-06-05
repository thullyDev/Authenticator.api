from sqlmodel import SQLModel

class user(SQLModel, table=True):
    id: int 
    username: str
    email: str
    token: str
