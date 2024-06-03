from typing import Any
from sqlmodel import create_engine
from decouple import config

SQL_URL: Any = config("SQL_URL")
engine = create_engine(SQL_URL)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# if __name__ == "__main__":
#     create_db_and_tables()