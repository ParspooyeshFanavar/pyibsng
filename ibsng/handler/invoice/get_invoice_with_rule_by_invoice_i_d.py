"""Get invoice with rule by invoice id API method."""
from ibsng.handler.handler import Handler


class getInvoiceWithRuleByInvoiceID(Handler):
    """Get invoice with rule by invoice id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.invoice_id, int)

    def setup(self, invoice_id):
        """Setup required parameters.

        :param int invoice_id: invoice id

        :return: None
        :rtype: None
        """
        self.invoice_id = invoice_id
