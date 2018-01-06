"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class loadPermsFromAnotherAdmin(Handler):
    """Admin Permission info method class."""

    def setup(self, admin_username, load_from_admin_username):
        """Setup required parameters.

        :param str admin_username: 
        :param str load_from_admin_username: 
    
        :return: void
        :rtype: void
        """
        self.admin_username = admin_username
        self.load_from_admin_username = load_from_admin_username
