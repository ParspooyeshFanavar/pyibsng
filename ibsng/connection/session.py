"""Main session handler library.

This library prepares session id for requests.
"""
import requests
from ibsng.setting import session as session_settings


class Session:
    """Session handler class."""

    _is_instance = None

    def __init__(self):
        """Session handler init."""
        self._session = requests.sessions.Session()
        self._session.headers.update(session_settings.SESSION_HEADERS)

    def __new__(cls, *args, **kwargs):
        """Singletone method to generate session."""
        if not cls._is_instance:
            cls._is_instance = object.__new__(Session, *args, **kwargs)
        return cls._is_instance

    def get_session(self):
        """Return current session.

        :return: current session
        :rtype: str
        """
        return self._session
