""" info API method."""
from ibsng.handler.handler import Handler


class updateAttributes(Handler):
    """ info method class."""

    def setup(self, ras_ip, attrs):
        """Setup required parameters.

        :param str ras_ip: 
        :param dict attrs: 
    
        :return: void
        :rtype: void
        """
        self.ras_ip = ras_ip
        self.attrs = attrs
