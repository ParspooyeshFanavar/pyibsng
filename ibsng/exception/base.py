"""IBSng base exceptions handler."""
import datetime


class IBSngException(Exception):
    """Base IBSng exception handler."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    _err_code = None

    def __init__(self, message):
        """Base IBSng exception handler.

        :param message: exception message
        :type message: str
        """
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