""" info API method."""
from ibsng.handler.handler import Handler


class getBWSnapShotForUserAjax(Handler):
    """ info method class."""

    def setup(self, from_=None, from_unit=None):
        """Setup required parameters.

        :param str from: by user
        :param str from_unit: 
    
        :return: void
        :rtype: void
        """
        self.from_ = from_
        self.from_unit = from_unit
