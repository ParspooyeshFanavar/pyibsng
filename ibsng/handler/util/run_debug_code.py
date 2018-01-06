""" info API method."""
from ibsng.handler.handler import Handler


class runDebugCode(Handler):
    """ info method class."""

    def setup(self, command):
        """Setup required parameters.

        :param str command: 
    
        :return: void
        :rtype: void
        """
        self.command = command
