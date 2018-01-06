""" info API method."""
from ibsng.handler.handler import Handler


class bulkKillUsers(Handler):
    """ info method class."""

    def setup(self, conds, kill=None):
        """Setup required parameters.

        :param dict conds: the same as method 'user.searchUser', parameter 'conds'
        :param bool kill: true means Kill User, false means Clear User
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.kill = kill
