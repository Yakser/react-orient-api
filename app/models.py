from sqlalchemy import Column, String, Integer

from app.database import Base


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    header = Column(String)
    date = Column(String)
    markup = Column(String)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    email = Column(String, unique=True)
    password = Column(String)
    username = Column(String)

    first_name = Column(String, default='')
    last_name = Column(String, default='')
    role = Column(String, default='')

#
# models
# # Created by Sergey Yaksanov at 07.10.2021
# Copyright © 2020 Yakser. All rights reserved.
