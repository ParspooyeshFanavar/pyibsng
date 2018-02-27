"""Voucher get batch by id API method."""
from ibsng.handler.handler import Handler


class voucherGetBatchByID(Handler):
    """Voucher get batch by id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.batch_id, str)

    def setup(self, batch_id):
        """Setup required parameters.

        :param int batch_id: batch id

        :return: None
        :rtype: None
        """
        self.batch_id = batch_id
