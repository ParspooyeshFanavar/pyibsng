""" info API method."""
from ibsng.handler.handler import Handler


class saveCreditChanges(Handler):
    """ info method class."""

    def setup(self, conds, cols, sort_by, desc, output_type):
        """Setup required parameters.

        :param dict conds: the same as getCreditChanges
        :param list cols: 
        :param choice sort_by: 
        :param bool desc: descending
        :param choice output_type: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.cols = cols
        self.sort_by = sort_by
        self.desc = desc
        self.output_type = output_type
