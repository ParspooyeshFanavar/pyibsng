""" info API method."""
from ibsng.handler.handler import Handler


class changeStatus(Handler):
    """ info method class."""

    def setup(self, user_id, status):
        """Setup required parameters.

        :param str user_id: 
        :param choice status: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.status = status
