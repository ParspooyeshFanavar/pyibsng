""" info API method."""
from ibsng.handler.handler import Handler


class getManagementSummaryReport(Handler):
    """ info method class."""

    def setup(self, conds):
        """Setup required parameters.

        :param dict conds: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
