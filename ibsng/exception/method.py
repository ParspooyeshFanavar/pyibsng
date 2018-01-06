"""IBSng method exceptions handler."""
from .base import IBSngException


class ServerMethodError(IBSngException):
    """Raise when method result contains error."""

    _err_code = 301

    def __init__(self, error_text):
        """Raise when method result contains error.

        :param error_text: server error body
        :type error_text: str
        """
        message = "Check your entries, server method returned error: {}"
        message = message.format(error_text)
        super(ServerMethodError, self).__init__(message)


class ImportMethodNotFound(IBSngException):
    """Raise when method file not found."""

    _err_code = 302

    def __init__(self, method_name):
        """Raise when method file not found.

        :param method_name: method name
        :type method_name: str
        """
        message = "There is no '{}' method in driver.".format(method_name)
        super(ImportMethodNotFound, self).__init__(message)


class ImportMethodError(IBSngException):
    """Raise when importing method encountered with error."""

    _err_code = 303

    def __init__(self, method_name):
        """Raise when importing method encountered with error.

        :param method_name: method name
        :type method_name: str
        """
        message = "Import {} method in driver got error.".format(method_name)
        super(ImportMethodError, self).__init__(message)
