from typing import List, Optional, Tuple
import psycopg2


class PostgresDB: 	
	def __init__(self, DB_URL: str) -> None:
		self.conn = psycopg2.connect(DB_URL)
		self.cursor = self.conn.cursor()

	def execute(self, query: str, params=None) -> bool:
		try:
			print(params)
			self.cursor.execute(query=query, vars=params)
			self.conn.commit()
			return True
		except psycopg2.Error as e:
			self.conn.rollback()

			print("Postgres Error: ", e)

			return False

	def fetch(self, query: str, params=None) -> Optional[List[Tuple]]:
		try:
			self.cursor.execute(query=query, vars=params)
			return self.cursor.fetchall()
		except psycopg2.Error as e:
			self.conn.rollback()

			print("Postgres Error: ", e)

			return None

	def close_connection(self):
		self.cursor.close()
		self.conn.close()
