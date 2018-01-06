"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class loadPermTemplateToAdmin(Handler):
    """Admin Permission info method class."""

    def setup(self, perm_template_name, admin_username):
        """Setup required parameters.

        :param str perm_template_name: 
        :param str admin_username: 
    
        :return: void
        :rtype: void
        """
        self.perm_template_name = perm_template_name
        self.admin_username = admin_username
