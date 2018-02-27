"""Get usernames API method."""
from ibsng.handler.handler import Handler


class getUsernames(Handler):
    """Get usernames method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.starts_with, str)

    def setup(self, starts_with):
        """Setup required parameters.

        :param str starts_with: starts with (name)

        :return: None
        :rtype: None
        """
        self.starts_with = starts_with
