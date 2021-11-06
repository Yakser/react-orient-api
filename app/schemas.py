from typing import Optional

from pydantic import BaseModel


class Base64File(BaseModel):
    file: str
    filename: str

class RegisterDetails(BaseModel):
    email: str
    password: str
    username: str


class LoginDetails(BaseModel):
    email: str
    password: str


class UsersCreate(BaseModel):
    email: str
    password: str
    username: str

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None


class Users(UsersCreate):
    id: int

    class Config:
        orm_mode = True


class NewsCreate(BaseModel):
    date: str
    header: str
    markup: str


class News(NewsCreate):
    id: int

    class Config:
        orm_mode = True
