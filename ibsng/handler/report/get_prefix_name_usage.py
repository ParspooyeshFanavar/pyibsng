""" info API method."""
from ibsng.handler.handler import Handler


class getPrefixNameUsage(Handler):
    """ info method class."""

    def setup(self, conds, from_, to_, order_by, desc):
        """Setup required parameters.

        :param dict conds: the same as 'report.getConnections' method
        :param int from: start index, for pagination
        :param int to: end index, for pagination
        :param choice order_by: 
        :param bool desc: descending
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.from_ = from_
        self.to_ = to_
        self.order_by = order_by
        self.desc = desc
