"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class issueProformaInvoice(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, attrs_list, arbitrary_amount):
        """Setup required parameters.

        :param list attrs_list: 
        :param float arbitrary_amount: 
    
        :return: void
        :rtype: void
        """
        self.attrs_list = attrs_list
        self.arbitrary_amount = arbitrary_amount
