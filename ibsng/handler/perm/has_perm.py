"""Has permission API method."""
from ibsng.handler.handler import Handler


class hasPerm(Handler):
    """Has permission method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.perm_name, str)
        self.is_valid(self.admin_username, str)

    def setup(self, perm_name, admin_username):
        """Setup required parameters.

        :param str perm_name: permission name
        :param str admin_username: admin username

        :return: None
        :rtype: None
        """
        self.perm_name = perm_name
        self.admin_username = admin_username
