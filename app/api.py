from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi import Depends
from app import schemas, models
from app.auth import AuthHandler
from app.database import get_db

auth_handler = AuthHandler()

news_router = SQLAlchemyCRUDRouter(
    schema=schemas.News,
    create_schema=schemas.NewsCreate,
    db_model=models.News,
    db=get_db,
    update_route=[Depends(auth_handler.auth_wrapper)],
    delete_all_route=[Depends(auth_handler.auth_wrapper)],
    delete_one_route=[Depends(auth_handler.auth_wrapper)],
    create_route=[Depends(auth_handler.auth_wrapper)]
)

users_router = SQLAlchemyCRUDRouter(
    schema=schemas.Users,
    create_schema=schemas.UsersCreate,
    db_model=models.Users,
    db=get_db,
    dependencies=[Depends(auth_handler.auth_wrapper)]
)
