"""Delete permission value API method."""
from ibsng.handler.handler import Handler


class delPermissionValue(Handler):
    """Delete permission value method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)
        self.is_valid(self.perm_name, str)
        self.is_valid(self.perm_value, str)

    def setup(self, admin_username, perm_name, perm_value):
        """Setup required parameters.

        :param str admin_username: admin_username
        :param str perm_name: permission name
        :param str perm_value: permission value

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
        self.perm_name = perm_name
        self.perm_value = perm_value
