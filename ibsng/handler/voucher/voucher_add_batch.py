"""Voucher and batch API method."""
from ibsng.handler.handler import Handler


class voucherAddBatch(Handler):
    """Voucher and batch method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.batch_dict, dict)
        self.is_valid(self.pin_prefix, str)
        self.is_valid(self.pin_len, int)
        self.is_valid(self.serial_prefix, str)
        self.is_valid(self.serial_start, int)
        self.is_valid(self.count, int)

    def setup(self, batch_dict, pin_prefix, pin_len,
              serial_prefix, serial_start, count):
        """Setup required parameters.

        :param dict batch_dict: batch dictionary
        :param str pin_prefix: pin prefix
        :param int pin_len: pin length
        :param str serial_prefix: serial prefix
        :param int serial_start: serial start
        :param int count: count

        :return: None
        :rtype: None
        """
        self.batch_dict = batch_dict
        self.pin_prefix = pin_prefix
        self.pin_len = pin_len
        self.serial_prefix = serial_prefix
        self.serial_start = serial_start
        self.count = count
