""" info API method."""
from ibsng.handler.handler import Handler


class getAllAdminInfos(Handler):
    """ info method class."""

    def setup(self, isp_name):
        """Setup required parameters.

        :param str isp_name: admins of specific ISP
    
        :return: void
        :rtype: void
        """
        self.isp_name = isp_name
