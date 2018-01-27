"""Change deposit extended API method."""
from ibsng.handler.handler import Handler


class changeDepositExtended(Handler):
    """Change deposit extended method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.credit, float)
        self.is_valid(self.change_type, str)
        self.is_valid_content(self.change_type, ("ADD|SET|MULTIPLY"))
        self.is_valid(self.credit_comment, str, False)

    def setup(self, user_id, deposit, change_type, deposit_comment=""):
        """Setup required parameters.

        :param str user_id: ibsng user id
        :param float deposit: new deposit value
        :param choice change_type: type of change (ADD, SET, MULTIPLY)
        :param str deposit_comment: omment for this deposit

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.deposit = deposit
        self.change_type = change_type
        self.deposit_comment = deposit_comment
