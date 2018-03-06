"""Message Center info API method."""
from ibsng.handler.handler import Handler


class activateService(Handler):
    """Message Center info method class."""

    def setup(self, cell_number):
        """Setup required parameters.

        :param str cell_number: cell phone number

        :return: None
        :rtype: None
        """
        self.cell_number = cell_number
