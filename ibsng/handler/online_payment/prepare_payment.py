""" info API method."""
from ibsng.handler.handler import Handler


class preparePayment(Handler):
    """ info method class."""

    def setup(self, gateway_type, amount, unique_id, callback_url, attributes):
        """Setup required parameters.

        :param choice gateway_type: 
        :param float amount: 
        :param str unique_id: 
        :param str callback_url: 
        :param dict attributes: you can put all the parameters you want here
    
        :return: void
        :rtype: void
        """
        self.gateway_type = gateway_type
        self.amount = amount
        self.unique_id = unique_id
        self.callback_url = callback_url
        self.attributes = attributes
