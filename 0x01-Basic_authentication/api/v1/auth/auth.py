#!/usr/bin/env python3
"""Auth Module"""

from flask import request


class Auth:
    """AUth Class"""
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """retuens false"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
