from typing import List, Tuple
import psycopg2


class PostgresDB: 	
	def __init__(self, DB_URL: str) -> None:
		self.conn = psycopg2.connect(DB_URL)
		self.cursor = self.conn.cursor()

	def execute(self, query: str, params=None) -> None:
		try:
			self.cursor.execute(query=query, vars=params)
			self.conn.commit()
		except psycopg2.Error as e:
			self.conn.rollback()
			raise(e)

	def fetch(self, query: str, params=None) -> List[Tuple]:
		try:
			self.cursor.execute(query=query, vars=params)
			return self.cursor.fetchall()
		except psycopg2.Error as e:
			self.conn.rollback()
			raise(e)

	def close_connection(self):
		self.cursor.close()
		self.conn.close()
