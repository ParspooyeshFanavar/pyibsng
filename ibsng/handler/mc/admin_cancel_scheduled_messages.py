"""Message Center info API method."""
from ibsng.handler.handler import Handler


class adminCancelScheduledMessages(Handler):
    """Message Center info method class."""

    def setup(self, message_ids):
        """Setup required parameters.

        :param int message_ids: 
    
        :return: void
        :rtype: void
        """
        self.message_ids = message_ids
