""" info API method."""
from ibsng.handler.handler import Handler


class getVoucherByID(Handler):
    """ info method class."""

    def setup(self, voucher_id):
        """Setup required parameters.

        :param int voucher_id: 
    
        :return: void
        :rtype: void
        """
        self.voucher_id = voucher_id
