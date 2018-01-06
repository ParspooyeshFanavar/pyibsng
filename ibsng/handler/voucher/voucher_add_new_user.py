""" info API method."""
from ibsng.handler.handler import Handler


class voucherAddNewUser(Handler):
    """ info method class."""

    def setup(self, voucher_pin, isp_name, group_name):
        """Setup required parameters.

        :param str voucher_pin: 
        :param str isp_name: 
        :param str group_name: 
    
        :return: void
        :rtype: void
        """
        self.voucher_pin = voucher_pin
        self.isp_name = isp_name
        self.group_name = group_name
