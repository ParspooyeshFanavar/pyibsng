""" info API method."""
from ibsng.handler.handler import Handler


class savePrefixNameUsage(Handler):
    """ info method class."""

    def setup(self, conds, order_by, desc, output_type):
        """Setup required parameters.

        :param dict conds: the same as 'report.getConnections' method
        :param choice order_by: 
        :param bool desc: descending
        :param choice output_type: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.order_by = order_by
        self.desc = desc
        self.output_type = output_type
