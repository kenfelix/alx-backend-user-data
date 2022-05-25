#!/usr/bin/env python3
"""Auth Module"""
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> bytes:
    """Returns a salted hash of
    the input password"""
    hashed_password = hashpw(password.encode('utf-8'), gensalt())

    return hashed_password
