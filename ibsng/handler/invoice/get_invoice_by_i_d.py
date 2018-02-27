"""Get invoice by id API method."""
from ibsng.handler.handler import Handler


class getInvoiceByID(Handler):
    """Get invoice by id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.invoice_id, int)

    def setup(self, invoice_id):
        """Setup required parameters.

        :param int invoice_id: ibsng invoice id

        :return: None
        :rtype: None
        """
        self.invoice_id = invoice_id
