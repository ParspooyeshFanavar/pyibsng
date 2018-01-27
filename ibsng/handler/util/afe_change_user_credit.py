"""AFE change user credit API method."""
from ibsng.handler.handler import Handler


class afeChangeUserCredit(Handler):
    """AFE change user credit method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.username, str)
        self.is_valid(self.amount, float)
        self.is_valid(self.comment, str, False)

    def setup(self, username, amount, comment=""):
        """Setup required parameters.

        :param str username: ibsng username
        :param float amount: user amount
        :param str comment: comment for this action

        :return: None
        :rtype: None
        """
        self.username = username
        self.amount = amount
        self.comment = comment
