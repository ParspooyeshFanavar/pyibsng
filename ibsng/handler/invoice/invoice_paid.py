"""Invoice paid API method."""
from ibsng.handler.handler import Handler


class invoicePaid(Handler):
    """Invoice paid method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.invoice_id_list, list)
        self.is_valid(self.paid_amount_list, list)
        self.is_valid(self.payment_comment_list, list)

    def setup(self, invoice_id_list, paid_amount_list, payment_comment_list):
        """Setup required parameters.

        :param list invoice_id_list: list of Invoice IDs
        :param list paid_amount_list: list of paid amounts, length of list must
                                      be the same as `invoice_id_list`
        :param list payment_comment_list: list of comment strings, length of
                                          list must be the same as
                                          `invoice_id_list`

        :return: None
        :rtype: None
        """
        self.invoice_id_list = invoice_id_list
        self.paid_amount_list = paid_amount_list
        self.payment_comment_list = payment_comment_list
