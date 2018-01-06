""" info API method."""
from ibsng.handler.handler import Handler


class getActiveRasIPs(Handler):
    """ info method class."""

    def setup(self, type_filter):
        """Setup required parameters.

        :param str type_filter: 
    
        :return: void
        :rtype: void
        """
        self.type_filter = type_filter
