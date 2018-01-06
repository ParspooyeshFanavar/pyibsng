""" info API method."""
from ibsng.handler.handler import Handler


class getUsernameForIP(Handler):
    """ info method class."""

    def setup(self, ip):
        """Setup required parameters.

        :param str ip: 
    
        :return: void
        :rtype: void
        """
        self.ip = ip
