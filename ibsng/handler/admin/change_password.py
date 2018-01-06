""" info API method."""
from ibsng.handler.handler import Handler


class changePassword(Handler):
    """ info method class."""

    def setup(self, admin_username, new_password):
        """Setup required parameters.

        :param str admin_username: 
        :param str new_password: 
    
        :return: void
        :rtype: void
        """
        self.admin_username = admin_username
        self.new_password = new_password
