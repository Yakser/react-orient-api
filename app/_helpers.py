from typing import Union

from app import models


def find_user_by_email(db, email: str) -> Union[type(models.Users), None]:
    """
    :param db: Instance of DB session
    :param email: String email value
    :return: Returns User instance or None if user with such email doesn't exists
    """
    return db.query(models.Users).filter(models.Users.email == email).first()
