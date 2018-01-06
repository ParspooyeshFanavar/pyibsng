"""Message Center info API method."""
from ibsng.handler.handler import Handler


class getRemoteRequestAttrs(Handler):
    """Message Center info method class."""

    def setup(self, type):
        """Setup required parameters.

        :param choice type: 
    
        :return: void
        :rtype: void
        """
        self.type = type
