""" info API method."""
from ibsng.handler.handler import Handler


class rechargeUsers(Handler):
    """ info method class."""

    def setup(self, user_id, comment):
        """Setup required parameters.

        :param str user_id: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.comment = comment
