""" info API method."""
from ibsng.handler.handler import Handler


class deleteRas(Handler):
    """ info method class."""

    def setup(self, ras_id):
        """Setup required parameters.

        :param int ras_id: 
    
        :return: void
        :rtype: void
        """
        self.ras_id = ras_id
