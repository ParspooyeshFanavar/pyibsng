""" info API method."""
from ibsng.handler.handler import Handler


class afeChangeUserCredit(Handler):
    """ info method class."""

    def setup(self, username, amount, comment):
        """Setup required parameters.

        :param str username: 
        :param float amount: 
        :param comment comment: 
    
        :return: void
        :rtype: void
        """
        self.username = username
        self.amount = amount
        self.comment = comment
