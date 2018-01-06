""" info API method."""
from ibsng.handler.handler import Handler


class getUsersWithCellPhone(Handler):
    """ info method class."""

    def setup(self, cell_phone):
        """Setup required parameters.

        :param str cell_phone: 
    
        :return: void
        :rtype: void
        """
        self.cell_phone = cell_phone
