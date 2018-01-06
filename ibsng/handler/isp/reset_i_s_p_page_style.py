""" info API method."""
from ibsng.handler.handler import Handler


class resetISPPageStyle(Handler):
    """ info method class."""

    def setup(self, isp_id):
        """Setup required parameters.

        :param int isp_id: 
    
        :return: void
        :rtype: void
        """
        self.isp_id = isp_id
