#!/usr/bin/env python3
"""
Module session_auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session authentication mechanism"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        return user_id_by_session_id.get(session_id)
