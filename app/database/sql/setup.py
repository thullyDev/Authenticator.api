from typing import Any, Optional
from decouple import config
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    deleted: bool = False
    created_at: datetime = Field(default=datetime.now())
    profile_image_url: Optional[str] = None
    token: Optional[str] = None
    # add or remove any attributes you want and dont want

SQL_URL: Any = config("SQL_URL") 
engine = create_engine(SQL_URL)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    users = [
        User(username='testUser', password='0000000000', email='testuser@example.com', deleted=False, token=''),
        User(username='testOwner', password='0000000000', email='testowner@example.com', deleted=False, token=''),
        User(username='thully', password='#200256@enoK', email='demykunta@gmail.com', deleted=False, token='')
    ]
    session.add_all(users)
    session.commit()

with Session(engine) as session:
    statement = select(User)
    result = session.exec(statement)
    users = result.fetchall()

    for user in users:
        print(user)
