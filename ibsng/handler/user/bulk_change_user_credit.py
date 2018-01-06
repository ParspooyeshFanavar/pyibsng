""" info API method."""
from ibsng.handler.handler import Handler


class bulkChangeUserCredit(Handler):
    """ info method class."""

    def setup(self, conds, credit, change_type, credit_comment):
        """Setup required parameters.

        :param dict conds: the same as method 'user.searchUser', parameter 'conds'
        :param float credit: the same as method 'user.changeCreditExtended'
        :param choice change_type: the same as method 'user.changeCreditExtended'
        :param str credit_comment: the same as method 'user.changeCreditExtended'
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.credit = credit
        self.change_type = change_type
        self.credit_comment = credit_comment
