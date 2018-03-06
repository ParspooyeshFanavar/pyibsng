"""Delete an admin API method."""
from ibsng.handler.handler import Handler


class deleteAdmin(Handler):
    """Delete an admin class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)

    def setup(self, admin_username):
        """Setup required parameters.

        :param str admin_username: admin authentication username

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
