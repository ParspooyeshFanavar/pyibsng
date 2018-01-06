"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class invoicePutUserOnDept(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, pi_id_list):
        """Setup required parameters.

        :param list pi_id_list: list of Proforma Invoice IDs
    
        :return: void
        :rtype: void
        """
        self.pi_id_list = pi_id_list
