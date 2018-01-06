""" info API method."""
from ibsng.handler.handler import Handler


class multiStrGetAll(Handler):
    """ info method class."""

    def setup(self, str, left_pad):
        """Setup required parameters.

        :param str str: 
        :param bool left_pad: 
    
        :return: void
        :rtype: void
        """
        self.str = str
        self.left_pad = left_pad
