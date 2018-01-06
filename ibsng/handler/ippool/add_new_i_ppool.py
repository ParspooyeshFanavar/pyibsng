""" info API method."""
from ibsng.handler.handler import Handler


class addNewIPpool(Handler):
    """ info method class."""

    def setup(self, ippool_name, comment):
        """Setup required parameters.

        :param str ippool_name: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.ippool_name = ippool_name
        self.comment = comment
