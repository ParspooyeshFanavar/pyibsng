"""Expire session API method."""
from ibsng.handler.handler import Handler


class expireSession(Handler):
    """Expire session method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.session_id, int)
        self.is_valid_content(self.session_id, self.ID_PATTERN)

    def setup(self, session_id):
        """Setup required parameters.

        :param str session_id: session id

        :return: None
        :rtype: None
        """
        self.session_id = session_id
