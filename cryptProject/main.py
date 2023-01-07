from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role

"""
create instance FastAPI
"""
app = FastAPI()


"""
create db
"""
db: List[User] = [
    User(
        id=uuid4(),
        first_name='Gilza',
        last_name='Goltz',
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name='Alex',
        last_name='Jones',
        gender=Gender.male,
        roles=[Role.admin]
    )
]


'''
get func extract data with get from root and return json
object in dictionary
'''


@app.get('/')
async def root():
    return {'Hello': 'Goltz'}


@app.get('/api/v1/users')
async def fetch_users():
    return db
