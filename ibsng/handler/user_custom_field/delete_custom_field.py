""" info API method."""
from ibsng.handler.handler import Handler


class deleteCustomField(Handler):
    """ info method class."""

    def setup(self, name):
        """Setup required parameters.

        :param str name: 
    
        :return: void
        :rtype: void
        """
        self.name = name
