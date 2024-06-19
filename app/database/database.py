from typing import Any, Dict, List, Optional
from app.database.models import SetUser, User
from app.resources.config import SQL_URL
from .sequel.postgresDatabase import PostgresDB 
import pprint

psqlDB: PostgresDB = PostgresDB(SQL_URL)  

def get_user(*, key: str, entity: str) -> Optional[User]:
	query = f"select * from \"user\" where {key} = '{entity}';"
	response = psqlDB.fetch(query=query)

	if not response:
		return None

	return User(response[0])

def set_user(user: SetUser) -> bool:
	keys = user.string_tuple("keys").replace("'", '')
	entities = user.string_tuple("entities").replace("None", "NULL")
	query = f"""
				insert into "user" {keys}
				values {entities};
			""".strip()

	res = psqlDB.execute(query)

	return res 

def update_user(*, key: str, entity: str, data: List[tuple[str, Any]]) -> bool:
	update_data = [f"set {column} = {repr(value)}" for column, value in data ]
	update_string = " , ".join(update_data)
	query = f"""
				update "user" 
				{update_string}
				where {key} = '{entity}';
			""".strip()
	return psqlDB.execute(query)
