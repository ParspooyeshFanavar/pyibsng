""" info API method."""
from ibsng.handler.handler import Handler


class getAuthData(Handler):
    """ info method class."""

    def setup(self, auth_session):
        """Setup required parameters.

        :param str auth_session: session_id
    
        :return: void
        :rtype: void
        """
        self.auth_session = auth_session
