"""Load perms from another admin API method."""
from ibsng.handler.handler import Handler


class savePermsOfAdminToTemplate(Handler):
    """Load perms from another admin method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)
        self.is_valid(self.perm_template_name, str)

    def setup(self, admin_username, perm_template_name):
        """Setup required parameters.

        :param str admin_username: admin username
        :param str perm_template_name: permission template name

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
        self.perm_template_name = perm_template_name
