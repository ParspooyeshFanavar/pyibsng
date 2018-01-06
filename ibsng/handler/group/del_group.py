""" info API method."""
from ibsng.handler.handler import Handler


class delGroup(Handler):
    """ info method class."""

    def setup(self, group_name):
        """Setup required parameters.

        :param str group_name: 
    
        :return: void
        :rtype: void
        """
        self.group_name = group_name
