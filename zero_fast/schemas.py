from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserResponse(BaseModel):
    username: str
    email: str


class UserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserResponse]
