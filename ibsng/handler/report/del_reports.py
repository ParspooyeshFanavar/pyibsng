""" info API method."""
from ibsng.handler.handler import Handler


class delReports(Handler):
    """ info method class."""

    def setup(self, table, date, date_unit):
        """Setup required parameters.

        :param str table: 
        :param str_datetime, float date: 
        :param choice date_unit: 
    
        :return: void
        :rtype: void
        """
        self.table = table
        self.date = date
        self.date_unit = date_unit
