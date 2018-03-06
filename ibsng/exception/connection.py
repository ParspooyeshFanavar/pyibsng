"""IBSng 'connection' exceptions handler."""
from .base import IBSngException


class InvalidConnectionString(IBSngException):
    """Raise when connection string pattern is not correct."""

    _err_code = 100

    def __init__(self):
        """Raise when connection string pattern is not correct."""
        message = "Invalid connection string structure. \
                   Structure is <host:port>@<username:password>"
        super(InvalidConnectionString, self).__init__(message)


class ServerConnectionError(IBSngException):
    """Raise when can't connect to the server."""

    _err_code = 101

    def __init__(self):
        """Raise when can't connect to the server."""
        message = "Server connection failed. Check your connection."
        super(ServerConnectionError, self).__init__(message)
