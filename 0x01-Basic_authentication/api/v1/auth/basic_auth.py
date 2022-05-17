#!/usr/bin/env python3
"""
Module basci_auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Inherits from Auth
    """
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header for a Basic Authentication"""
        if authorization_header and type(authorization_header) == str and authorization_header.startswith('Basic'):
            return authorization_header.split(" ")[-1]
        return None
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string base64_authorization_header"""
        if not base64_authorization_header and type(base64_authorization_header):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except:
            None
        
