""" info API method."""
from ibsng.handler.handler import Handler


class getOnlineUsersCountLoop(Handler):
    """ info method class."""

    def setup(self, conds=None):
        """Setup required parameters.

        :param dict conds: the same as getOnlineUsers
    
        :return: void
        :rtype: void
        """
        self.conds = conds
