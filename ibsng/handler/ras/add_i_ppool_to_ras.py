""" info API method."""
from ibsng.handler.handler import Handler


class addIPpoolToRas(Handler):
    """ info method class."""

    def setup(self, ras_ip, ippool_name):
        """Setup required parameters.

        :param str ras_ip: 
        :param str ippool_name: 
    
        :return: void
        :rtype: void
        """
        self.ras_ip = ras_ip
        self.ippool_name = ippool_name
