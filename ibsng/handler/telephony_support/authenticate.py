""" info API method."""
from ibsng.handler.handler import Handler


class authenticate(Handler):
    """ info method class."""

    def setup(self, auth_by, auth_id):
        """Setup required parameters.

        :param choice auth_by: 
        :param str auth_id: 
    
        :return: void
        :rtype: void
        """
        self.auth_by = auth_by
        self.auth_id = auth_id
