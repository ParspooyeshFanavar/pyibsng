""" info API method."""
from ibsng.handler.handler import Handler


class addNewCharge(Handler):
    """ info method class."""

    def setup(self, charge_name, comment, isp_name):
        """Setup required parameters.

        :param str charge_name: 
        :param str comment: 
        :param str isp_name: 
    
        :return: void
        :rtype: void
        """
        self.charge_name = charge_name
        self.comment = comment
        self.isp_name = isp_name
