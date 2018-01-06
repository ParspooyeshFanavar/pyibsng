""" info API method."""
from ibsng.handler.handler import Handler


class changeCreditExtended(Handler):
    """ info method class."""

    def setup(self, user_id, credit, change_type, credit_comment):
        """Setup required parameters.

        :param str user_id: 
        :param float credit: 
        :param choice change_type: 
        :param str credit_comment: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.credit = credit
        self.change_type = change_type
        self.credit_comment = credit_comment
