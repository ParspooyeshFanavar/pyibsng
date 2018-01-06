""" info API method."""
from ibsng.handler.handler import Handler


class changeInternetPassword(Handler):
    """ info method class."""

    def setup(self, user_id, new_internet_password):
        """Setup required parameters.

        :param int user_id: 
        :param str new_internet_password: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.new_internet_password = new_internet_password
