"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class changePermission(Handler):
    """Admin Permission info method class."""

    def setup(self, admin_username, perm_name, perm_value):
        """Setup required parameters.

        :param str admin_username: 
        :param str perm_name: 
        :param str perm_value: 
    
        :return: void
        :rtype: void
        """
        self.admin_username = admin_username
        self.perm_name = perm_name
        self.perm_value = perm_value
