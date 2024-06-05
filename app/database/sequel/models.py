from typing import Any, Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

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
