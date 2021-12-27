import base64
import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from os import environ

from app.database import engine, get_db

from . import models
from ._helpers import find_user_by_email
from .api import news_router, users_router
from .auth import AuthHandler
from .schemas import Base64File, LoginDetails, RegisterDetails

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "https://react-orient.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(news_router)
app.include_router(users_router)

auth_handler = AuthHandler()


@app.post("/upload")
async def create_upload_file(file: Base64File, email=Depends(auth_handler.auth_wrapper), folder: str = "2021"):
    file_content = base64.b64decode(file.file.split(',')[1])
    with open(f"static/{folder}/{file.filename}", "wb") as f:
        f.write(file_content)


@app.post('/register', status_code=201)
def register(auth_details: RegisterDetails, db: Session = Depends(get_db)):
    user = find_user_by_email(db=db, email=auth_details.email)
    if user:
        raise HTTPException(
            status_code=400, detail='Account with this email already exists')

    hashed_password = auth_handler.get_password_hash(auth_details.password)
    new_user = models.Users(email=auth_details.email,
                            password=hashed_password, username=auth_details.username)
    db.add(new_user)
    db.commit()

    return {'message': 'ok'}


@app.post('/login')
def login(auth_details: LoginDetails, db: Session = Depends(get_db)):
    user = find_user_by_email(db=db, email=auth_details.email)

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user.password)):
        raise HTTPException(
            status_code=401, detail='Invalid email and/or password')

    token = auth_handler.encode_token(user.email)

    return {'token': token}


@app.get('/')
def index():
    return {'message': "home page"}


@app.get('/files')
def index():
    folder = "./static/"
    all_files = []
   
    for subdir, dirs, files in os.walk(folder):
        if files:
            all_files += [subdir + '/' + file for file in files]
   
    return {'files': all_files}


@app.get('/verify')
def verify(email=Depends(auth_handler.auth_wrapper)):
    return {'message': 'ok'}
