from typing import Any, Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False, max_length=100)
    email: str = Field(nullable=False, max_length=100, unique=True)
    password: str = Field(nullable=False, max_length=100, min_length=10)
    deleted: bool = False
    created_at: datetime = Field(default=datetime.now())
    profile_image_url: Optional[str] = Field(default=None, max_length=300)
    token: Optional[str] = Field(default=None, max_length=300)
    
    # add or remove any attributes you want and dont want
