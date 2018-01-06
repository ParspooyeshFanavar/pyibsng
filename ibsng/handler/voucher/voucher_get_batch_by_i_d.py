""" info API method."""
from ibsng.handler.handler import Handler


class voucherGetBatchByID(Handler):
    """ info method class."""

    def setup(self, batch_id):
        """Setup required parameters.

        :param int batch_id: 
    
        :return: void
        :rtype: void
        """
        self.batch_id = batch_id
