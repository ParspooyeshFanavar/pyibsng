"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class getPermsOfAdmin(Handler):
    """Admin Permission info method class."""

    def setup(self, admin_username):
        """Setup required parameters.

        :param str admin_username: 
    
        :return: void
        :rtype: void
        """
        self.admin_username = admin_username
