""" info API method."""
from ibsng.handler.handler import Handler


class searchOTPs(Handler):
    """ info method class."""

    def setup(self, conds, _from, to_, sort_by, desc):
        """Setup required parameters.

        :param dict conds: 
        :param int _from: page start index
        :param int to: page end index
        :param choice sort_by: 
        :param bool desc: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self._from = _from
        self.to_ = to_
        self.sort_by = sort_by
        self.desc = desc
