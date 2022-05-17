#!/usr/bin/env python3
"""Auth Module"""

from flask import request
from typing import List, TypeVar



class Auth:
    """AUth Class"""
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """retuens false"""
        if path in excluded_paths:
            return False
        if not path or not excluded_paths:
            return True
        if path[-1] != '/' and path + '/'\
                in excluded_paths:
            return False
        
    
    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
