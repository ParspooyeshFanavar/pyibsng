""" info API method."""
from ibsng.handler.handler import Handler


class getISPTree(Handler):
    """ info method class."""

    def setup(self, isp_name=None):
        """Setup required parameters.

        :param str isp_name: if this param is missing, we use admin's owner ISP
    
        :return: void
        :rtype: void
        """
        self.isp_name = isp_name
