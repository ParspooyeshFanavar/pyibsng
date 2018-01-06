""" info API method."""
from ibsng.handler.handler import Handler


class getUsersWithPhone(Handler):
    """ info method class."""

    def setup(self, phone):
        """Setup required parameters.

        :param str phone: 
    
        :return: void
        :rtype: void
        """
        self.phone = phone
