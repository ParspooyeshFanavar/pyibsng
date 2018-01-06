""" info API method."""
from ibsng.handler.handler import Handler


class voucherChangeBatchLockStatus(Handler):
    """ info method class."""

    def setup(self, batch_id, lock):
        """Setup required parameters.

        :param int batch_id: 
        :param bool lock: 
    
        :return: void
        :rtype: void
        """
        self.batch_id = batch_id
        self.lock = lock
