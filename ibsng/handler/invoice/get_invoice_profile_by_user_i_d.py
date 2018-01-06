"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class getInvoiceProfileByUserID(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, user_id):
        """Setup required parameters.

        :param int user_id: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
