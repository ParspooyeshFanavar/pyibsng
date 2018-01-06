""" info API method."""
from ibsng.handler.handler import Handler


class changeDepositExtended(Handler):
    """ info method class."""

    def setup(self, user_id, deposit, change_type, deposit_comment):
        """Setup required parameters.

        :param str user_id: 
        :param float deposit: 
        :param choice change_type: 
        :param str deposit_comment: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.deposit = deposit
        self.change_type = change_type
        self.deposit_comment = deposit_comment
