"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class savePermsOfAdminToTemplate(Handler):
    """Admin Permission info method class."""

    def setup(self, admin_username, perm_template_name):
        """Setup required parameters.

        :param str admin_username: 
        :param str perm_template_name: 
    
        :return: void
        :rtype: void
        """
        self.admin_username = admin_username
        self.perm_template_name = perm_template_name
