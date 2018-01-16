"""Get ISP of an admin AIP method."""
from ibsng.handler.handler import Handler


class getAdminISPID(handler):
    """Get ISP ID of an admin class."""

    def setup(self, admin_username):
        """Setup required parameters.

        :param str admin_username: admin authentication username

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
