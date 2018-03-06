"""Get info of all admins API method."""
from ibsng.handler.handler import Handler


class getAllAdminInfos(Handler):
    """Get info of all admins class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        if getattr(self, "isp_name"):
            self.is_valid(self.isp_name, str)

    def setup(self, isp_name=None):
        """Setup required parameters.

        :param str isp_name: admins of specific ISP

        :return: None
        :rtype: None
        """
        if isp_name:
            self.isp_name = isp_name
