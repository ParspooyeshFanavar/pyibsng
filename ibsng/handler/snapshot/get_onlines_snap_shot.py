""" info API method."""
from ibsng.handler.handler import Handler


class getOnlinesSnapShot(Handler):
    """ info method class."""

    def setup(self, conds, type):
        """Setup required parameters.

        :param dict conds: 
        :param choice type: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.type = type
