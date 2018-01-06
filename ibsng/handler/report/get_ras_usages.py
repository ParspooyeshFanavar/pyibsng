""" info API method."""
from ibsng.handler.handler import Handler


class getRasUsages(Handler):
    """ info method class."""

    def setup(self, conds):
        """Setup required parameters.

        :param dict conds: the same as 'report.getConnections' method
    
        :return: void
        :rtype: void
        """
        self.conds = conds
