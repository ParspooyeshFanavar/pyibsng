"""IBSng 'method' exceptions handler."""
from .base import IBSngException


class ServerMethodError(IBSngException):
    """Raise when method result contains error."""

    _err_code = 401

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

    _err_code = 402

    def __init__(self, method_name):
        """Raise when method file not found.

        :param method_name: method name
        :type method_name: str
        """
        message = "There is no '{}' method in driver.".format(method_name)
        super(ImportMethodNotFound, self).__init__(message)


class ImportMethodError(IBSngException):
    """Raise when importing method encountered with error."""

    _err_code = 403

    def __init__(self, method_name):
        """Raise when importing method encountered with error.

        :param method_name: method name
        :type method_name: str
        """
        message = "Import {} method in driver got error.".format(method_name)
        super(ImportMethodError, self).__init__(message)


class InvalidArgumentType(IBSngException):
    """Raise when method argument type is incorrect."""

    _err_code = 404

    def __init__(self, method_name, argument_value, argument_type):
        """Raise when method argument type is incorrect.

        :param str method_name: method name
        :param str argument_value: argument value
        :param str argument_type: argument type
        """
        message = "Method '{}' got incorrect argument type: '{}' ({})".\
                  format(method_name, argument_value, argument_type.__name__)
        super(InvalidArgumentType, self).__init__(message)


class InvalidArgumentValue(IBSngException):
    """Raise when method argument value is incorrect format."""

    _err_code = 405

    def __init__(self, method_name, argument_value, regex_pattern=""):
        """Raise when method argument value is incorrect format.

        :param str method_name: method name
        :param type argument_value: argument data
        :param type regex_pattern: regular expression pattern
        """
        if not regex_pattern:
            message = "Method '{}' got empty argument value: '{}'".\
                      format(method_name, argument_value)
        else:
            message = "Method '{}' got incorrect argument value: '{}' ({})".\
                      format(method_name, argument_value, regex_pattern)
        super(InvalidArgumentValue, self).__init__(message)
