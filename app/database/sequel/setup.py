from typing import Any
from decouple import config
from sqlmodel import SQLModel, create_engine

SQL_URL: Any = config("SQL_URL") 
engine = create_engine(SQL_URL)

SQLModel.metadata.create_all(engine)