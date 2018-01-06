""" info API method."""
from ibsng.handler.handler import Handler


class getISPInfo(Handler):
    """ info method class."""

    def setup(self, isp_name=None, isp_id=None):
        """Setup required parameters.

        :param str isp_name: 
        :param int isp_id: added in C_312
    
        :return: void
        :rtype: void
        """
        self.isp_name = isp_name
        self.isp_id = isp_id
