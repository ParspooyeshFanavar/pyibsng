"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class addInvoiceTemplate(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, template_name):
        """Setup required parameters.

        :param str template_name: 
    
        :return: void
        :rtype: void
        """
        self.template_name = template_name
