from fastapi import FastAPI, HTTPException, status
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


class UserUpdate(User):
    date_joined: Optional[date] = None
    age: int = Field(None, gt=5, lt=200)


def ensure_username_in_db(username: str):
    """
    if username not in database he has exception with code 404
    """
    if username not in user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Username {username} not found.')


app = FastAPI()


@app.get('/users')
async def get_users_query(limit: int = 20):
    """
    This func shows all users
    """
    user_list = list(user_db.values())
    return user_list[:limit]


@app.get('/users/{username}')
async def get_users_path(username: str):
    """
    This func shows certain user from db
    """
    if username not in user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Username {username} not found.')
    return user_db[username]


@app.post('/users')
async def create_user(user: User):
    """
    This func accept info from user and create user
    """
    username = user.username
    ensure_username_in_db(username)
    user_db[username] = user.dict()
    return {'message': f'Successfully created user: {username}'}


@app.delete('/users/{username}')
async def delete_user(username: str):
    """
    this func delete user
    """
    ensure_username_in_db(username)
    del user_db[username]
    return {'message': f'Successfully deleted user: {username}'}


@app.put('/users')
async def update_user(user: User):
    """
    replace the ALL data by username
    EVERYTHING IS CHANGING
    """
    username = user.username
    ensure_username_in_db(username)
    user_db[username] = user.dict()
    return {'message': f'Successfully update user: {username}'}


@app.patch('/users')
async def update_user_partial(user: UserUpdate):
    """
    replace the PARTIAL data by username
    PART IS CHANGING

    exclude_unset for fields with value None(like an age)

    >>user_db[username].update(user.dict(exclude_unset=True))
    >>part change

    >>user_db[username].update(user.dict())
    >>without exclude_unset changes all

    >>user_db[username] = (user.dict(exclude_unset=True))
    >>deleted not changed fields
    """
    username = user.username
    ensure_username_in_db(username)
    user_db[username].update(user.dict(exclude_unset=True))
    return {'message': f'Successfully update user: {username}'}


# post does the same as patch above
#
# ??? can there be only one post ???
#
# @app.post('/users')
# async def update_user_partial_post(user: User):
#     username = user.username
#     user_db[username].update(user.dict(exclude_unset=True))
#     return {'message': f'Successfully update user: {username}'}
