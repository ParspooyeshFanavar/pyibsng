"""Message Center info API method."""
from ibsng.handler.handler import Handler


class adminDeleteMessage(Handler):
    """Message Center info method class."""

    def setup(self, message_ids, target_box):
        """Setup required parameters.

        :param int message_ids: 
        :param choice target_box: 
    
        :return: void
        :rtype: void
        """
        self.message_ids = message_ids
        self.target_box = target_box
