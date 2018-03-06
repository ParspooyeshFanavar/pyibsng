"""IBSng 'handler' exceptions handler."""
from .base import IBSngException


class HandlerNotFound(IBSngException):
    """Raise when handler directory not found."""

    _err_code = 301

    def __init__(self, handler_name):
        """Raise when handler directory not found.

        :param handler_name: handler name
        :type handler_name: str
        """
        message = "There is no '{}' handler in driver.".format(handler_name)
        super(HandlerNotFound, self).__init__(message)
