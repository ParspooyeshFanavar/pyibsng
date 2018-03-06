"""Get permissions of admin API method."""
from ibsng.handler.handler import Handler


class getPermsOfAdmin(Handler):
    """Get permissions of admin method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)

    def setup(self, admin_username):
        """Setup required parameters.

        :param str admin_username: admin username

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
