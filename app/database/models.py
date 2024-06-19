from datetime import datetime
from typing import Any, Optional, Tuple, Union

#! please use this is order when initializing using a tuple, or else the attributes wont match

class BaseUser:
	def entities_to_tuple(self) -> Tuple[
			 int,
			 str,
			 str,
			 str,
			 bool,
			 datetime,
			 Optional[str],
			 Optional[str]
		]:
		return tuple(vars(self).values())


	def keys_to_tuple(self, as_strings=False) -> Tuple[str, ...]:
		return tuple(self.__dict__.keys()) 

	def string_tuple(self, type) -> str:
		if type == "keys":
			return str(self.keys_to_tuple())

		if type == "entities":
			return str(self.entities_to_tuple())

		raise Exception(f"no such type: {type}, try keys or entities")

class User(BaseUser):
	def __init__(self, user: Tuple[
			int,
			str,
			str,
			str,
			bool,
			datetime,
			Optional[str],
			str]
		):
		self.id: int = user[0] 
		self.username: str = user[1]
		self.email: str = user[2]
		self.password: str = user[3]
		self.deleted: bool = user[4]
		self.profile_image_url: Optional[str] = user[6]
		self.token: Optional[str] = user[7]

class SetUser(BaseUser):
	def __init__(self, user: Tuple[str, ...]):
		self.username: str = user[0]
		self.email: str = user[1]
		self.password: str = user[2]
		self.token: str = user[3]

