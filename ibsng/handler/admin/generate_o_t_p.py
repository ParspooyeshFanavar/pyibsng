""" info API method."""
from ibsng.handler.handler import Handler


class generateOTP(Handler):
    """ info method class."""

    def setup(self, pass_len, pass_count, admin_username):
        """Setup required parameters.

        :param int pass_len: 
        :param int pass_count: 
        :param str admin_username: 
    
        :return: void
        :rtype: void
        """
        self.pass_len = pass_len
        self.pass_count = pass_count
        self.admin_username = admin_username
