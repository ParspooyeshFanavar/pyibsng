"""Change deposit API method."""
from ibsng.handler.handler import Handler


class changeDeposit(Handler):
    """Change deposit method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.deposit, float)
        self.is_valid(self.is_absolute_change, bool)
        self.is_valid(self.deposit_comment, str, False)

    def setup(self, user_id, deposit, is_absolute_change, deposit_comment=""):
        """Setup required parameters.

        :param str user_id: ibsng user id
        :param float deposit: new deposit
        :param bool is_absolute_change: 'false' for relative change (add to
                                         user's deposit), 'true' for absolute
                                         change (set user's deposit)
        :param str deposit_comment: comment for this action

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.deposit = deposit
        self.is_absolute_change = is_absolute_change
        self.deposit_comment = deposit_comment
