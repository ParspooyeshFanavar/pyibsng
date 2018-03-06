""" info API method."""
from ibsng.handler.handler import Handler


class getConnectionUsages(Handler):
    """ info method class."""

    def setup(self, conds, from_, to_, order_by):
        """Setup required parameters.

        :param dict conds: the same as 'report.getConnections' method
        :param int from: start index, for pagination
        :param int to: end index, for pagination
        :param choice order_by: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.from_ = from_
        self.to_ = to_
        self.order_by = order_by
