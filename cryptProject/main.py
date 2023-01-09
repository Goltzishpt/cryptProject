from fastapi import FastAPI

app = FastAPI()


user_db = {
    'jack': {'username': 'jack', 'date_joined': '2023-01-08', 'location': 'Toronto', 'age': 28},
    'jill': {'username': 'jill', 'date_joined': '2023-01-07', 'location': 'NY', 'age': 29},
    'jane': {'username': 'jane', 'date_joined': '2023-01-06', 'location': 'LA', 'age': 19}
}


@app.get('/users')
def get_users():
    user_list = list(user_db.values())
    return user_list


@app.get('/users/{username}')
def get_users_path(username: str):
    return user_db[username]