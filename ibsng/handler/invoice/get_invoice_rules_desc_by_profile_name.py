"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class getInvoiceRulesDescByProfileName(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, profile_name):
        """Setup required parameters.

        :param str profile_name: 
    
        :return: void
        :rtype: void
        """
        self.profile_name = profile_name
