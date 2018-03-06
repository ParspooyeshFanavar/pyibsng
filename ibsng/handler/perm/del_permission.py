"""Delete permission API method."""
from ibsng.handler.handler import Handler


class delPermission(Handler):
    """Delete permission method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)
        self.is_valid(self.perm_name, str)

    def setup(self, admin_username, perm_name):
        """Setup required parameters.

        :param str admin_username: admin username
        :param str perm_name: permission name

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
        self.perm_name = perm_name
