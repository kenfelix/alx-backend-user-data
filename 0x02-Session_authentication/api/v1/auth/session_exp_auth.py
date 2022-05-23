#!/usr/bin/env python3
"""
Module session_auth
"""
from api.v1.auth.session_auth.py import SessionAuth
from sys import getenv
from datetime import datetime


class SessionExpAuth(SessionAuth):
    """SessionExpAuth that inherits from SessionAuth"""

    def __init__(self):
        """instatializes the class"""
        SESSION_DURATION = getenv('SESSION_DURATION')
        if not SESSION_DURATION or type(SESSION_DURATION) != int:
            self.session_duration = 0
        self.session_duration = int(SESSION_DURATION)

    def create_session(self, user_id=None):
        """Create user session"""
        created_at = datetime.now()
        session_dic = {"user_id": user_id, "created_at": created_at}
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        SessionAuth.user_id_by_session_id[session_id] = session_dic
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """return user_id from the session dictionary"""
        if session_id is None or \
                SessionAuth.user_id_by_session_id.has_key(session_id) is False:
            return None
        if self.session_duration <= 0:
            return '"user_id"
        if self.session_dic.has_key(created_at) is False:
            return None
        if (self.session_dic.get(created_at) + session_duration) < datetime.now:
            return None
        return self.session_dic.get('user_id')
