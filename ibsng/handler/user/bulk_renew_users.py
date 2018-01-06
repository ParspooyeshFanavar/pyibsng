""" info API method."""
from ibsng.handler.handler import Handler


class bulkRenewUsers(Handler):
    """ info method class."""

    def setup(self, conds, renew_comment):
        """Setup required parameters.

        :param dict conds: the same as method 'user.searchUser', parameter 'conds'
        :param str renew_comment: the same as method 'user.renewUsers', parameter 'comment'
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.renew_comment = renew_comment
