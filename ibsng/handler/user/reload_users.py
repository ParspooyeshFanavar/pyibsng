"""Reload users API method."""
from ibsng.handler.handler import Handler


class reloadUsers(Handler):
    """Reload users method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, str)
        self.is_valid_content(self.user_id, self.IDS_PATTERN)

    def setup(self, user_ids):
        """Setup required parameters.

        :param list user_ids: ibsng user ids

        :return: None
        :rtype: None
        """
        self.user_id = ",".join(map(str, user_ids))
