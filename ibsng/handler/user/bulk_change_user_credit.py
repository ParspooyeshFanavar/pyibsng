"""Bulk change user credit API method."""
from ibsng.handler.handler import Handler


class bulkChangeUserCredit(Handler):
    """Bulk change user credit method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.credit, float)
        self.is_valid(self.change_type, str)
        self.is_valid_content(self.change_type, ("ADD|SET|MULTIPLY"))
        self.is_valid(self.credit_comment, str, False)

    def setup(self, conds, credit, change_type, credit_comment=""):
        """Setup required parameters.

        :param dict conds: conditions
        :param float credit: initialize credit
        :param str change_type: change action type
        :param str credit_comment: comment for credit

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.credit = credit
        self.change_type = change_type
        self.credit_comment = credit_comment
