"""Message Center info API method."""
from ibsng.handler.handler import Handler


class dialerDeleteMessage(Handler):
    """Message Center info method class."""

    def setup(self, message_id):
        """Setup required parameters.

        :param int message_id: 
    
        :return: void
        :rtype: void
        """
        self.message_id = message_id
