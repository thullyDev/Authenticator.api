from typing import Sequence, Union
from sqlalchemy.orm.loading import instances
from sqlmodel import Session, select, SQLModel
from .setup import engine

def set(*, model) -> SQLModel:
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

def update(*, model, id, update_item) -> Union[SQLModel, None]:
	return None
	# with Session(engine) as session:
	# 	instance = session.get(model, id)

	# 	if not instance:
	# 		return None
	# 	hero_data = update_item.model_dump(exclude_unset=True)
	# 	instance.sqlmodel_update(model)
	# 	session.add(instance)
	# 	session.commit()
	# 	session.refresh(instance)

	# 	return instance

# @app.patch("/heroes/{hero_id}", response_model=HeroPublic)
# def update_hero(hero_id: int, hero: HeroUpdate):
#     with Session(engine) as session:
#         db_hero = session.get(Hero, hero_id)
#         if not db_hero:
#             raise HTTPException(status_code=404, detail="Hero not found")
#         hero_data = hero.model_dump(exclude_unset=True)
#         db_hero.sqlmodel_update(hero_data)
#         session.add(db_hero)
#         session.commit()
#         session.refresh(db_hero)
#         return db_hero
        
def delete(*, model, **kwargs) -> bool:
	with Session(engine) as session:
		# instance = session.query(model).filter_by(**kwargs).first()
		instance = session.get(model, **kwargs)

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

