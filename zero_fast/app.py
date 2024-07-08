from http import HTTPStatus

from fastapi import FastAPI
from schemas import Message, UserResponse, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundão'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserResponse)
def create_user(user: UserSchema):
    return user
