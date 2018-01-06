"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class canDo(Handler):
    """Admin Permission info method class."""

    def setup(self, perm_name, admin_username, params):
        """Setup required parameters.

        :param str perm_name: 
        :param str admin_username: 
        :param list params: 
    
        :return: void
        :rtype: void
        """
        self.perm_name = perm_name
        self.admin_username = admin_username
        self.params = params
