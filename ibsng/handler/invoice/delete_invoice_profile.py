"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class deleteInvoiceProfile(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, profile_id):
        """Setup required parameters.

        :param int profile_id: 
    
        :return: void
        :rtype: void
        """
        self.profile_id = profile_id
