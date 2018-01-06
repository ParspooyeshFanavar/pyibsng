""" info API method."""
from ibsng.handler.handler import Handler


class saveConnectionUsages(Handler):
    """ info method class."""

    def setup(self, report_type, conds, cols, sort_by, output_type):
        """Setup required parameters.

        :param choice report_type: 
        :param dict conds: the same as 'report.getConnections' method
        :param list cols: 
        :param choice sort_by: 
        :param choice output_type: 
    
        :return: void
        :rtype: void
        """
        self.report_type = report_type
        self.conds = conds
        self.cols = cols
        self.sort_by = sort_by
        self.output_type = output_type
