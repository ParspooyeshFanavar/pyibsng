""" info API method."""
from ibsng.handler.handler import Handler


class deleteGateway(Handler):
    """ info method class."""

    def setup(self, gateway_name):
        """Setup required parameters.

        :param str gateway_name: 
    
        :return: void
        :rtype: void
        """
        self.gateway_name = gateway_name
