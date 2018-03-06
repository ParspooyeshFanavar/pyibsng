"""IBSng 'authentication' exceptions handler."""
from .base import IBSngException


class InvalidAuthentication(IBSngException):
    """Raise when user authentication failed."""

    _err_code = 501

    def __init__(self):
        """Raise when user authentication failed."""
        message = "Authentication failed. Check username or password."
        super(InvalidAuthentication, self).__init__(message)


class InvalidSessionId(IBSngException):
    """Raise when user session id is invalid."""

    _err_code = 502

    def __init__(self):
        """Raise when user session id is invalid."""
        message = "User session id is invalid. Login again."
        super(InvalidSessionId, self).__init__(message)
