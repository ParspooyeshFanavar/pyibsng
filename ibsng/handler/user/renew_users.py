"""Renew users API method."""
from ibsng.handler.handler import Handler


class renewUsers(Handler):
    """Renew users method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, str)
        self.is_valid_content(self.user_id, self.IDS_PATTERN)
        self.is_valid(self.comment, str, False)

    def setup(self, user_ids, comment=""):
        """Setup required parameters.

        :param list user_ids: ibsng user ids
        :param str comment: comment for this action

        :return: None
        :rtype: None
        """
        self.user_id = ",".join(map(str, user_ids))
        self.comment = comment
