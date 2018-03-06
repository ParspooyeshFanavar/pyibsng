"""IBSng base exceptions handler.

Exception numbers (starts with):
    1: connections
    2: generals
    3: handlers
    4: methods
    5: authentication
    6: unknown
"""
import datetime


class IBSngException(Exception):
    """Base IBSng exception handler."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _err_code = None

    def __init__(self, message):
        """Base IBSng exception handler.

        :param message: exception message
        :type message: str
        """
        self._err_msg = message
        message = "[{}]:{} - {}".format(self.timestamp,
                                        message,
                                        self._err_code)
        super(IBSngException, self).__init__(message)

    @property
    def error_code(self):
        """Return exception error code.

        :return: exception error code
        :rtype: int
        """
        return self._err_code

    @property
    def error_msg(self):
        """Return exception error message.

        :return: exception error message
        :rtype: str
        """
        return self._err_msg
