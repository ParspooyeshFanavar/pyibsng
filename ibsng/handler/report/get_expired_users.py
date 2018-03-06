""" info API method."""
from ibsng.handler.handler import Handler


class getExpiredUsers(Handler):
    """ info method class."""

    def setup(self, conds, from_, to_, sort_by, desc):
        """Setup required parameters.

        :param dict conds: the same as user.searchUser
        :param int from: start index
        :param int to: end index
        :param choice sort_by: 
        :param bool desc: descending
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.from_ = from_
        self.to_ = to_
        self.sort_by = sort_by
        self.desc = desc
