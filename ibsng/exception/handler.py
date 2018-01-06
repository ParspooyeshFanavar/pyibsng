"""IBSng 'handler' exceptions handler."""
from .base import IBSngException


class ImportHandlerNotFound(IBSngException):
    """Raise when handler directory not found."""

    _err_code = 201

    def __init__(self, handler_name):
        """Raise when handler directory not found.

        :param handler_name: handler name
        :type handler_name: str
        """
        message = "There is no '{}' handler in driver.".format(handler_name)
        super(ImportHandlerNotFound, self).__init__(message)
