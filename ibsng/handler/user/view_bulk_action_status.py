""" info API method."""
from ibsng.handler.handler import Handler


class viewBulkActionStatus(Handler):
    """ info method class."""

    def setup(self, action_id):
        """Setup required parameters.

        :param str action_id: 
    
        :return: void
        :rtype: void
        """
        self.action_id = action_id
