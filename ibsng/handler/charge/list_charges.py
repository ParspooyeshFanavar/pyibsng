""" info API method."""
from ibsng.handler.handler import Handler


class listCharges(Handler):
    """ info method class."""

    def setup(self, isp_id):
        """Setup required parameters.

        :param str isp_id: comma-seprated. list of isp ids
    
        :return: void
        :rtype: void
        """
        self.isp_id = isp_id
