from typing import Sequence, Union
from sqlmodel import Session, select, SQLModel
from .setup import engine

def set(model) -> SQLModel:
	with Session(engine) as session:
		session.add(model)
		session.commit()
		session.refresh(model)
		return model

def setall(models) -> None:
	with Session(engine) as session:
		session.add_all(models)
		session.commit()

def get(*, model, **kwargs) -> Union[SQLModel, None]:
	with Session(engine) as session:
		instance = session.query(model).filter_by(**kwargs).first()

		if not instance:
			return None
		return instance

def update(*, model, **kwargs) -> Union[SQLModel, None]:
	with Session(engine) as session:
		instance = session.query(model).filter_by(**kwargs).first()

		if not instance:
			return None

		instance.sqlmodel_update(model)
		session.add(instance)
		session.commit()
		session.refresh(instance)

		return instance

def delete(*, model, **kwargs) -> bool:
	with Session(engine) as session:
		instance = session.query(model).filter_by(**kwargs).first()

		if not instance:
			return False

		session.delete(instance)
		session.commit()
		return True

def getall(*, model) -> Sequence:
	with Session(engine) as session:
		data = session.exec(select(model)).all()
		return data
		
def get_query(*, model, **kwargs) -> Sequence[SQLModel]:
	with Session(engine) as session:
		data = session.exec(select(model).filter_by(**kwargs)).all()
		return data

