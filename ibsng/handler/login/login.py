""" info API method."""
from ibsng.handler.handler import Handler


class login(Handler):
    """ info method class."""

    def setup(self, login_auth_type, login_auth_name, login_auth_pass):
        """Setup required parameters.

        :param choice login_auth_type: 
        :param str login_auth_name: 
        :param str login_auth_pass: 
    
        :return: void
        :rtype: void
        """
        self.login_auth_type = login_auth_type
        self.login_auth_name = login_auth_name
        self.login_auth_pass = login_auth_pass
