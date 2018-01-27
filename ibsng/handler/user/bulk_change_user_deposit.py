"""Bulk change user API method."""
from ibsng.handler.handler import Handler


class bulkChangeUserDeposit(Handler):
    """Bulk change user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.deposit, float)
        self.is_valid(self.change_type, str)
        self.is_valid_content(self.change_type, ("ADD|SET|MULTIPLY"))
        self.is_valid(self.deposit_comment, str, False)

    def setup(self, conds, deposit, change_type, deposit_comment=""):
        """Setup required parameters.

        :param dict conds: conditions
        :param float deposit: initialize deposit
        :param str change_type: change action type
        :param str credit_comment: comment for credit

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.deposit = deposit
        self.change_type = change_type
        self.deposit_comment = deposit_comment
