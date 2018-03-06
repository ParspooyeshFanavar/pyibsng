"""Get ISP of an admin AIP method."""
from ibsng.handler.handler import Handler


class getAdminISPID(Handler):
    """Get ISP ID of an admin class."""

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
