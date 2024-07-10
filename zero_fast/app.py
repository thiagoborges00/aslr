from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from .schemas import Message, UserList, UserResponse, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundão'}


@app.post('/users', status_code=HTTPStatus.CREATED,
          response_model=UserResponse)
def create_user(user: UserSchema):
    return user


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def list_users():
    return {'users': database}


@app.put('/users/{user_id}', status_code=HTTPStatus.OK,
         response_model=UserResponse)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='User not found')
    return {""}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='User not found')
    return {"message": "User deleted"}
