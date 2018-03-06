"""Load permission template to admin info API method."""
from ibsng.handler.handler import Handler


class loadPermTemplateToAdmin(Handler):
    """Load permission template to admin method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.perm_template_name, str)
        self.is_valid(self.admin_username, str)

    def setup(self, perm_template_name, admin_username):
        """Setup required parameters.

        :param str perm_template_name:  permission template name
        :param str admin_username: admin username

        :return: None
        :rtype: None
        """
        self.perm_template_name = perm_template_name
        self.admin_username = admin_username
