""" info API method."""
from ibsng.handler.handler import Handler


class checkInternetPassword(Handler):
    """ info method class."""

    def setup(self, user_id, internet_password):
        """Setup required parameters.

        :param int user_id: 
        :param str internet_password: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.internet_password = internet_password
