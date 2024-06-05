from .sql import sql, models 


userModel = models.user
sql = sql.Sql()

users = sql.sql_get_all(model=userModel)

print(users)