""" info API method."""
from ibsng.handler.handler import Handler


class changeISPDeposit(Handler):
    """ info method class."""

    def setup(self, isp_name, deposit_amount, comment):
        """Setup required parameters.

        :param str isp_name: 
        :param float deposit_amount: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.isp_name = isp_name
        self.deposit_amount = deposit_amount
        self.comment = comment
