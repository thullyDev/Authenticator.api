from typing import Dict, Any, List, Sequence, Union
from sqlmodel import Session, select, SQLModel
from .setup import engine

class Sql:
	def sql_set(self, model) -> SQLModel:
		with Session(engine) as session:
			session.add(model)
			session.commit()
			session.refresh(model)
			return model

	def sql_set_all(self, models) -> None:
		with Session(engine) as session:
			session.add_all(models)
			session.commit()

	def sql_get(self, model, **kwargs) -> Union[SQLModel, None]:
		with Session(engine) as session:
			instance = session.get(model, **kwargs)
			if not instance:
				return None
			return instance

	def sql_update(self, model, **kwargs) -> Union[SQLModel, None]:
		with Session(engine) as session:
			instance = session.get(model, **kwargs)

			if not instance:
				return None

			instance.sqlmodel_update(model)
			session.add(instance)
			session.commit()
			session.refresh(instance)

			return instance

	def sql_delete(self, model, **kwargs) -> bool:
		with Session(engine) as session:
			instance = session.get(model, **kwargs)

			if not instance:
				return False

			session.delete(instance)
			session.commit()
			return True

	def sql_get_all(self, model) -> Sequence:
		with Session(engine) as session:
			data = session.exec(select(model)).all()
			return data
			
	def sql_get_query(self, model, **kwargs) -> Sequence:
		with Session(engine) as session:
			data = session.exec(select(model).filter(**kwargs)).all()
			return data
