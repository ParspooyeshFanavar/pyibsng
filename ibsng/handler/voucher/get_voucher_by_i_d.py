"""Get voucher by id API method."""
from ibsng.handler.handler import Handler


class getVoucherByID(Handler):
    """Get voucher by id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.voucher_id, int)

    def setup(self, voucher_id):
        """Setup required parameters.

        :param int voucher_id: voucher id

        :return: None
        :rtype: None
        """
        self.voucher_id = voucher_id
