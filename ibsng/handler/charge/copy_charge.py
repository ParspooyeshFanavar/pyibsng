""" info API method."""
from ibsng.handler.handler import Handler


class copyCharge(Handler):
    """ info method class."""

    def setup(self, charge_name, comment, copy_count):
        """Setup required parameters.

        :param str charge_name: 
        :param str comment: 
        :param int copy_count: 
    
        :return: void
        :rtype: void
        """
        self.charge_name = charge_name
        self.comment = comment
        self.copy_count = copy_count
