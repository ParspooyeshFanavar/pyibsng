""" info API method."""
from ibsng.handler.handler import Handler


class getRequestTopStats(Handler):
    """ info method class."""

    def setup(self, order_by):
        """Setup required parameters.

        :param choice order_by: 
    
        :return: void
        :rtype: void
        """
        self.order_by = order_by
