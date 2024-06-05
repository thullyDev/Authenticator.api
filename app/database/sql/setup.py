from typing import Any, Optional
from decouple import config
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    deleted: bool = False
    created_at: datetime = Field(default=datetime.now())
    profile_image_url: Optional[str] = None
    token: Optional[str] = None
    # add or remove any attributes you want and dont want

SQL_URL: Any = config("SQL_URL") 
engine = create_engine(SQL_URL)

SQLModel.metadata.create_all(engine)