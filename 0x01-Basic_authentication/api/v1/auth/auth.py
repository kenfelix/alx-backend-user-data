#!/usr/bin/env python3
"""Auth Module"""

from flask import request
from typing import List, TypeVar



class Auth:
    """AUth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """retuens false"""
        if not path or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        if path[-1] != '/' and path + '/'\
                in excluded_paths:
            return False
        for p in excluded_paths:
            if p.endswith('*') and\
                    path.startswith(p[:-1]):
                return False
        return True


    def authorization_header(self, request=None) -> str:
        """returns None"""
        if not request or not request.headers or\
                not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
