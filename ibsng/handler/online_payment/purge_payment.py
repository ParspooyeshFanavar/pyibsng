""" info API method."""
from ibsng.handler.handler import Handler


class purgePayment(Handler):
    """ info method class."""

    def setup(self, payment_id):
        """Setup required parameters.

        :param int payment_id: 
    
        :return: void
        :rtype: void
        """
        self.payment_id = payment_id
