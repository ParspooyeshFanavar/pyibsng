"""All LDAP methods info API method."""
from ibsng.handler.handler import Handler


class getUserInfo(Handler):
    """All LDAP methods info method class."""

    def setup(self, username):
        """Setup required parameters.

        :param str username: 
    
        :return: void
        :rtype: void
        """
        self.username = username
