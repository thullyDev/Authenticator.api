from typing import Dict
from app.resources.config import SQL_URL
from .sequel.postgresDatabase import PostgresDB 

sqlDB: PostgresDB = PostgresDB(SQL_URL)  

def get_user() -> Dict[str, str]:
	return {}

def set_user() -> None:
	pass

def update_user() -> None:
	pass