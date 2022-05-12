#!/usr/bin/env python3
""" Encrypt passwords"""
import bcrypt
from typing import Callable


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def is_valid(hashed_password: Callable, password: str) -> bool:
    """check if password is valid"""
    return True if bcrypt.checkpw(password.encode(), hashed_password) else False
