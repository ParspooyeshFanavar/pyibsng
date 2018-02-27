"""Performa invoice paid API method."""
from ibsng.handler.handler import Handler


class proformaInvoicePaid(Handler):
    """Performa invoice paid method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.pi_id_list, list)
        self.is_valid_content(self.pi_id_list, self.ID_PATTERN)
        self.is_valid(self.paid_amount_list, list)
        # FIXME: need validate amount value (int, float or ...)
        self.is_valid(self.payment_comment_list, list)

    def setup(self, pi_id_list, paid_amount_list, payment_comment_list):
        """Setup required parameters.

        :param list pi_id_list: list of proforma invoice ids
        :param list paid_amount_list: list of paid amounts, length of list must
                                      be the same as `pi_id_list`
        :param list payment_comment_list: list of comment strings, length of
                                          list must be the same as `pi_id_list`

        :return: None
        :rtype: None
        """
        self.pi_id_list = pi_id_list
        self.paid_amount_list = paid_amount_list
        self.payment_comment_list = payment_comment_list
