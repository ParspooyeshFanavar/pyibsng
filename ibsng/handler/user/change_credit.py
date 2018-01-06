""" info API method."""
from ibsng.handler.handler import Handler


class changeCredit(Handler):
    """ info method class."""

    def setup(self, user_id, credit, is_absolute_change, credit_comment):
        """Setup required parameters.

        :param str user_id: 
        :param float credit: 
        :param bool is_absolute_change: 'false' for relative change (add to user's credit), 'true' for absolute change (set user's credit)
        :param str credit_comment: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.credit = credit
        self.is_absolute_change = is_absolute_change
        self.credit_comment = credit_comment
