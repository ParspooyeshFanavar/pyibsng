""" info API method."""
from ibsng.handler.handler import Handler


class changeDeposit(Handler):
    """ info method class."""

    def setup(self, user_id, deposit, is_absolute_change, deposit_comment):
        """Setup required parameters.

        :param str user_id: 
        :param float deposit: 
        :param bool is_absolute_change: 'false' for relative change (add to user's deposit), 'true' for absolute change (set user's deposit)
        :param str deposit_comment: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.deposit = deposit
        self.is_absolute_change = is_absolute_change
        self.deposit_comment = deposit_comment
