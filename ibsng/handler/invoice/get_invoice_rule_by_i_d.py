"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class getInvoiceRuleByID(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, rule_id):
        """Setup required parameters.

        :param int rule_id: 
    
        :return: void
        :rtype: void
        """
        self.rule_id = rule_id
