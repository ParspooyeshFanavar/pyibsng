"""Message Center info API method."""
from ibsng.handler.handler import Handler


class receive(Handler):
    """Message Center info method class."""

    def setup(self, msg_info):
        """Setup required parameters.

        :param dict msg_info: 
    
        :return: void
        :rtype: void
        """
        self.msg_info = msg_info
