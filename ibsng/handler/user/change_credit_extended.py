"""Change credit extended API method."""
from ibsng.handler.handler import Handler


class changeCreditExtended(Handler):
    """Change credit extended method class."""

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

    def setup(self, user_id, credit, change_type, credit_comment=""):
        """Setup required parameters.

        :param str user_id: ibsng user id
        :param float credit: new credit value
        :param str change_type: type of change (ADD, SET, MULTIPLY)
        :param str credit_comment: comment for this credit

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.credit = credit
        self.change_type = change_type
        self.credit_comment = credit_comment
