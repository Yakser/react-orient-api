from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DB_URL = "sqlite:///./database.db"

engine = create_engine("sqlite:///./database.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()
#
# database
# # Created by Sergey Yaksanov at 07.10.2021
# Copyright © 2020 Yakser. All rights reserved.
