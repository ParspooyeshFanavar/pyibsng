"""Check user existence API method."""
from ibsng.handler.handler import Handler


class doesUserExists(Handler):
    """Check user existence method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.normal_username, str)

    def setup(self, normal_username):
        """Setup required parameters.

        :param str normal_username: ibsng normal username

        :return: None
        :rtype: None
        """
        self.normal_username = normal_username
