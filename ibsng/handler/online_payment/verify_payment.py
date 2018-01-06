""" info API method."""
from ibsng.handler.handler import Handler


class verifyPayment(Handler):
    """ info method class."""

    def setup(self, unique_id, web_attributes):
        """Setup required parameters.

        :param str unique_id: 
        :param dict web_attributes: 
    
        :return: void
        :rtype: void
        """
        self.unique_id = unique_id
        self.web_attributes = web_attributes
