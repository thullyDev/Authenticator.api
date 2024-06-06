from typing import Optional
from sqlmodel import SQLModel
from .sequel import User, sql

def get_user(**kwargs) -> Optional[SQLModel]:
	user = sql.get(model=User, **kwargs)

	return user

def set_user(**kwargs) -> Optional[SQLModel]:
	user = User(**kwargs)

	return sql.set(model=user)

def update_user(**kwargs) -> Optional[SQLModel]:
	user = User(**kwargs)
	return sql.update(model=user, **kwargs)