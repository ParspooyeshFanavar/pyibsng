"""Message Center info API method."""
from ibsng.handler.handler import Handler


class adminCancelScheduledMessages(Handler):
    """Message Center info method class."""

    def setup(self, message_ids):
        """Setup required parameters.

        :param list message_ids: message ids

        :return: None
        :rtype: None
        """
        self.message_ids = ",".join(map(str,message_ids))
