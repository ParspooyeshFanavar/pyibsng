""" info API method."""
from ibsng.handler.handler import Handler


class getIPpoolNames(Handler):
    """ info method class."""

    def setup(self, ippool_type):
        """Setup required parameters.

        :param choice ippool_type: 
    
        :return: void
        :rtype: void
        """
        self.ippool_type = ippool_type
