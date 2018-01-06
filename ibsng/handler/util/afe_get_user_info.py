""" info API method."""
from ibsng.handler.handler import Handler


class afeGetUserInfo(Handler):
    """ info method class."""

    def setup(self, username):
        """Setup required parameters.

        :param str username: 
    
        :return: void
        :rtype: void
        """
        self.username = username
