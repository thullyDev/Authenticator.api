from .sequel import User, sql

def get_user(**kwargs):
	user = sql.get(model=User, **kwargs)

	return user
