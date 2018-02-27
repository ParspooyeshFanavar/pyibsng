"""Voucher change batch lock status API method."""
from ibsng.handler.handler import Handler


class voucherChangeBatchLockStatus(Handler):
    """Voucher change batch lock status method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.batch_id, int)
        self.is_valid(self.lock, bool)

    def setup(self, batch_id, lock):
        """Setup required parameters.

        :param int batch_id: batch id
        :param bool lock: lock

        :return: None
        :rtype: None
        """
        self.batch_id = batch_id
        self.lock = lock
