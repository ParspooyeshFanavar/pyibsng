"""IBSng 'general' exceptions handler."""
from .base import IBSngException


class ChainFormatError(IBSngException):
    """Raise when method or handler called in invalid chain format."""

    _err_code = 201

    def __init__(self, chain_list):
        """Raise when method or handler called in invalid chain format.

        :param chain_list: list of all chain items
        :type chain_list: list
        """
        message = "Chain format '{}' is incorrect format.".format(chain_list)
        super(ChainFormatError, self).__init__(message)
