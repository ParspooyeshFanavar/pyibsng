"""Get all username of admins API method."""
from ibsng.handler.handler import Handler


class getAllAdminUsernames(Handler):
    """Get all username of admins class."""

    def setup(self, isp_name=None):
        """Setup required parameters.

        :param str isp_name: isp name (optional) 

        :return: None
        :rtype: None
        """
        if isp_name:
            self.isp_name = isp_name
