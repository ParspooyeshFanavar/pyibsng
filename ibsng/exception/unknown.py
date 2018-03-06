"""IBSng 'unknown' exceptions handler."""
from .base import IBSngException


class UnknownError(IBSngException):
    """Raise when method result contains unknown error."""

    _err_code = 601

    def __init__(self, error_text):
        """Raise when method result contains unknown error.

        :param error_text: method error body
        :type error_text: str
        """
        message = "Server method returned unknown error: {}"
        message = message.format(error_text)
        super(UnknownError, self).__init__(message)
