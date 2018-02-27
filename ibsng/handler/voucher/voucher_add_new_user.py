"""Voucher add new user API method."""
from ibsng.handler.handler import Handler


class voucherAddNewUser(Handler):
    """Voucher add new user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.voucher_pin, str)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.group_name, str)

    def setup(self, voucher_pin, isp_name, group_name):
        """Setup required parameters.

        :param str voucher_pin: voucher pin
        :param str isp_name: isp name
        :param str group_name: group name

        :return: None
        :rtype: None
        """
        self.voucher_pin = voucher_pin
        self.isp_name = isp_name
        self.group_name = group_name
