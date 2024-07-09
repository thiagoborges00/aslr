from http import HTTPStatus

from fastapi import FastAPI
from  .schemas import Message, UserResponse, UserSchema, UserList

app = FastAPI()

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundão'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserResponse)
def create_user(user: UserSchema):
    return user


@app.get('/users',status_code=HTTPStatus.OK, response_class=UserList)
def list_users():
    return {'users': database}


@app.delete('/users')
def delete_user(user: UserSchema):
    return {"message": "excluído"}