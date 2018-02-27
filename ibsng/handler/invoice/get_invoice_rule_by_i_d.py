"""Get invoice by rule id API method."""
from ibsng.handler.handler import Handler


class getInvoiceRuleByID(Handler):
    """Get invoice by rule id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.rule_id, int)

    def setup(self, rule_id):
        """Setup required parameters.

        :param int rule_id: ibsng rule id

        :return: None
        :rtype: None
        """
        self.rule_id = rule_id
