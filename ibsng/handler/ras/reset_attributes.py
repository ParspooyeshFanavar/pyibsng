""" info API method."""
from ibsng.handler.handler import Handler


class resetAttributes(Handler):
    """ info method class."""

    def setup(self, ras_ip):
        """Setup required parameters.

        :param str ras_ip: 
    
        :return: void
        :rtype: void
        """
        self.ras_ip = ras_ip
