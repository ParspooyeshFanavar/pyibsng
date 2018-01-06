""" info API method."""
from ibsng.handler.handler import Handler


class getBatchVoucherAttrs(Handler):
    """ info method class."""

    def setup(self, voucher_pin):
        """Setup required parameters.

        :param str voucher_pin: 
    
        :return: void
        :rtype: void
        """
        self.voucher_pin = voucher_pin
