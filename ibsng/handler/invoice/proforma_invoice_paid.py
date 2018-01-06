"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class proformaInvoicePaid(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, pi_id_list, paid_amount_list, payment_comment_list):
        """Setup required parameters.

        :param list pi_id_list: list of Proforma Invoice IDs
        :param list paid_amount_list: list of paid amounts, length of list must be the same as `pi_id_list`
        :param list payment_comment_list: list of comment strings, length of list must be the same as `pi_id_list`
    
        :return: void
        :rtype: void
        """
        self.pi_id_list = pi_id_list
        self.paid_amount_list = paid_amount_list
        self.payment_comment_list = payment_comment_list
