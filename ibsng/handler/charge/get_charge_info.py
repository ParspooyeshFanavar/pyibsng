""" info API method."""
from ibsng.handler.handler import Handler


class getChargeInfo(Handler):
    """ info method class."""

    def setup(self, charge_name):
        """Setup required parameters.

        :param str charge_name: 
    
        :return: void
        :rtype: void
        """
        self.charge_name = charge_name
