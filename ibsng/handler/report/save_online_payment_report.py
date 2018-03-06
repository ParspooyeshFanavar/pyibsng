""" info API method."""
from ibsng.handler.handler import Handler


class saveOnlinePaymentReport(Handler):
    """ info method class."""

    def setup(self, conds, sort_by, desc, output_type):
        """Setup required parameters.

        :param dict conds: the same as 'report.getOnlinePaymentReport' method
        :param choice sort_by: 
        :param bool desc: descending
        :param choice output_type: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.sort_by = sort_by
        self.desc = desc
        self.output_type = output_type
