#!/usr/bin/env python3
"""Auth Module"""
from db import DB
from user import User
from typing import Union
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Returns a salted hash of
    the input password"""
    hashed_password = hashpw(password.encode('utf-8'), gensalt())

    return hashed_password


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    uid = str(uuid4())
    return uid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """creates a new user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def create_session(self, email: str) -> str:
        """returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def valid_login(self, email: str, password: str) -> bool:
        """returns true if user is valid"""
        try:
            user= self._db.find_user_by(email=email)
            return checkpw(
                    password.encode('utf-8'),
                    user.hashed_password
                    )
        except NoResultFound:
            return False

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        finds a user using the session id
        """
        if session_id is None:
            return None
        
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
