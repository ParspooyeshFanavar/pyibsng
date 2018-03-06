"""Temporary extend users API method."""
from ibsng.handler.handler import Handler


class temporaryExtendUsers(Handler):
    """Temporary extend users method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, str)
        self.is_valid_content(self.user_id, self.IDS_PATTERN)
        self.is_valid(self.temporary_extend_hours, int)
        self.is_valid(self.temporary_extend_credit, float)

    def setup(self, user_ids, temporary_extend_hours, temporary_extend_credit):
        """Setup required parameters.

        :param list user_ids: ibsng user ids
        :param int temporary_extend_hours: hours
        :param float temporary_extend_credit: credit

        :return: None
        :rtype: None
        """
        self.user_id = ",".join(map(str, user_ids))
        self.temporary_extend_hours = temporary_extend_hours
        self.temporary_extend_credit = temporary_extend_credit
