from typing import Dict, Optional
from app.database.models import SetUser, User
from app.resources.config import SQL_URL
from .sequel.postgresDatabase import PostgresDB 

psqlDB: PostgresDB = PostgresDB(SQL_URL)  

def get_user(*, key: str, entity: str) -> Optional[User]:
	query = f"select * from \"user\" where {key} = '{entity}';"
	response = psqlDB.fetch(query=query)

	if response == None:
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

def update_user(*, key: str, entity: str, column: str, value: str) -> bool:
	query = f"""
				update "user" 
				set {column} = {repr(value)} 
				where {key} = '{entity}';
			""".strip()

	res = psqlDB.execute(query)

	return res 


# UPDATE employees
# SET salary = 50000
# WHERE name = 'John';