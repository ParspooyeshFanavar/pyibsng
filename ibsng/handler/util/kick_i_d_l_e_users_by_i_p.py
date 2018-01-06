""" info API method."""
from ibsng.handler.handler import Handler


class kickIDLEUsersByIP(Handler):
    """ info method class."""

    def setup(self, idle_ip_list):
        """Setup required parameters.

        :param list idle_ip_list: list of IP string
    
        :return: void
        :rtype: void
        """
        self.idle_ip_list = idle_ip_list
