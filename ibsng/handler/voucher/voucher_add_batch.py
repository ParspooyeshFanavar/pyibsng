""" info API method."""
from ibsng.handler.handler import Handler


class voucherAddBatch(Handler):
    """ info method class."""

    def setup(self, batch_dict, pin_prefix, pin_len, serial_prefix, serial_start, count):
        """Setup required parameters.

        :param dict batch_dict: 
        :param str pin_prefix: 
        :param int pin_len: 
        :param str serial_prefix: 
        :param int serial_start: 
        :param int count: 
    
        :return: void
        :rtype: void
        """
        self.batch_dict = batch_dict
        self.pin_prefix = pin_prefix
        self.pin_len = pin_len
        self.serial_prefix = serial_prefix
        self.serial_start = serial_start
        self.count = count
