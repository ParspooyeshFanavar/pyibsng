""" info API method."""
from ibsng.handler.handler import Handler


class expireSession(Handler):
    """ info method class."""

    def setup(self, session_id):
        """Setup required parameters.

        :param str session_id: 
    
        :return: void
        :rtype: void
        """
        self.session_id = session_id
