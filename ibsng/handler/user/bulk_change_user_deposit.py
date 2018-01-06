""" info API method."""
from ibsng.handler.handler import Handler


class bulkChangeUserDeposit(Handler):
    """ info method class."""

    def setup(self, conds, deposit, change_type, deposit_comment):
        """Setup required parameters.

        :param dict conds: the same as method 'user.searchUser', parameter 'conds'
        :param float deposit: the same as method 'user.changeDepositExtended'
        :param choice change_type: the same as method 'user.changeDepositExtended'
        :param str deposit_comment: the same as method 'user.changeDepositExtended'
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.deposit = deposit
        self.change_type = change_type
        self.deposit_comment = deposit_comment
