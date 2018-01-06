""" info API method."""
from ibsng.handler.handler import Handler


class getIPpoolInfo(Handler):
    """ info method class."""

    def setup(self, ippool_name):
        """Setup required parameters.

        :param str ippool_name: 
    
        :return: void
        :rtype: void
        """
        self.ippool_name = ippool_name
