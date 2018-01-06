"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class getInvoiceProfileByGroupName(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, group_name):
        """Setup required parameters.

        :param str group_name: 
    
        :return: void
        :rtype: void
        """
        self.group_name = group_name
