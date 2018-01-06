"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class getInvoiceWithRuleByInvoiceID(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, invoice_id):
        """Setup required parameters.

        :param int invoice_id: 
    
        :return: void
        :rtype: void
        """
        self.invoice_id = invoice_id
