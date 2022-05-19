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
        if not user_id or type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        user_id_by_session_id[session_id] = user_id
        return session_id
