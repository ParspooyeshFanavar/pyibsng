"""Get auth data API method."""
from ibsng.handler.handler import Handler


class getAuthData(Handler):
    """Get auth data method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.auth_session, int)
        self.is_valid_content(self.auth_session, self.ID_PATTERN)

    def setup(self, session_id):
        """Setup required parameters.

        :param str auth_session: session id

        :return: None
        :rtype: None
        """
        self.auth_session = session_id
