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
            
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if not decoded_base64_authorization_header or type(decoded_base64_authorization_header) != str or ":" not in decoded_base64_authorization_header:
            return None, None
        
        value = decoded_base64_authorization_header.split(":")
        
        return value[0], value[1]
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if not user_email or type(user_email) != str:
            return None
        if not user_pwd or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            return None
        
    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        header = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(base64)
        credentials = self.extract_user_credentials(decoded)
        user = user = self.user_object_from_credentials(*credentials)

        return user
