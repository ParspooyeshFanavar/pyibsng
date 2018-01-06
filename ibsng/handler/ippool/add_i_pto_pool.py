""" info API method."""
from ibsng.handler.handler import Handler


class addIPtoPool(Handler):
    """ info method class."""

    def setup(self, ippool_name, ip):
        """Setup required parameters.

        :param str ippool_name: 
        :param str ip: 
    
        :return: void
        :rtype: void
        """
        self.ippool_name = ippool_name
        self.ip = ip
