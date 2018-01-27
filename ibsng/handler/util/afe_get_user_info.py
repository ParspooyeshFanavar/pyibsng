"""AFE get user info API method."""
from ibsng.handler.handler import Handler


class afeGetUserInfo(Handler):
    """AFE get user info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.username, str)

    def setup(self, username):
        """Setup required parameters.

        :param str username: ibsng username

        :return: None
        :rtype: None
        """
        self.username = username
