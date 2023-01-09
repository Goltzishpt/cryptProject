from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


user_db = {
    'jack': {'username': 'jack', 'date_joined': '2023-01-08', 'location': 'Toronto', 'age': 28},
    'jill': {'username': 'jill', 'date_joined': '2023-01-07', 'location': 'NY', 'age': 29},
    'jane': {'username': 'jane', 'date_joined': '2023-01-06', 'location': 'LA', 'age': 19}
}


class User(BaseModel):
    """
    User model with parameters:
    age: gt >, lt <, ge >=, le <=
    """
    username: str = Field(min_length=3, max_length=20)
    date_joined: date
    location: Optional[str] = None
    age: int = Field(None, gt=5, lt=130)


app = FastAPI()


@app.get('/users')
def get_users_query(limit: int = 20):
    """
    This func shows all users
    """
    user_list = list(user_db.values())
    return user_list[:limit]


@app.get('/users/{username}')
def get_users_path(username: str):
    """
    This func shows certain user from db
    """
    return user_db[username]


@app.post('/users')
def create_user(user: User):
    """
    This func accept info from user and create user
    """
    username = user.username
    user_db[username] = user.dict()
    return {'message': f'Successfully created user: {username}'}
