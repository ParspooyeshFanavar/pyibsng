""" info API method."""
from ibsng.handler.handler import Handler


class echo(Handler):
    """ info method class."""

    def setup(self, echo):
        """Setup required parameters.

        :param str echo: 
    
        :return: void
        :rtype: void
        """
        self.echo = echo
