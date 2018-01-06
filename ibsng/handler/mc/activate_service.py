"""Message Center info API method."""
from ibsng.handler.handler import Handler


class activateService(Handler):
    """Message Center info method class."""

    def setup(self, cell_number):
        """Setup required parameters.

        :param str cell_number: 
    
        :return: void
        :rtype: void
        """
        self.cell_number = cell_number
