""" info API method."""
from ibsng.handler.handler import Handler


class doesUserExists(Handler):
    """ info method class."""

    def setup(self, normal_username):
        """Setup required parameters.

        :param str normal_username: 
    
        :return: void
        :rtype: void
        """
        self.normal_username = normal_username
