"""Change user credit API method."""
from ibsng.handler.handler import Handler


class changeCredit(Handler):
    """Change user credit method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.credit, float)
        self.is_valid(self.is_absolute_change, bool)
        self.is_valid(self.credit_comment, str, False)

    def setup(self, user_id, credit, is_absolute_change, credit_comment=""):
        """Setup required parameters.

        :param str user_id: ibsng user id
        :param float credit: new credit value
        :param bool is_absolute_change: 'false' for relative change (add to
                                        user's credit), 'true' for absolute
                                        change (set user's credit)
        :param str credit_comment: comment for this credit

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.credit = credit
        self.is_absolute_change = is_absolute_change
        self.credit_comment = credit_comment
