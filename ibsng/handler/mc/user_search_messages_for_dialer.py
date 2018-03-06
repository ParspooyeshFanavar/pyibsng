"""Message Center info API method."""
from ibsng.handler.handler import Handler


class userSearchMessagesForDialer(Handler):
    """Message Center info method class."""

    def setup(self, from_, to_, order_by, desc):
        """Setup required parameters.

        :param int from: 
        :param int to: 
        :param choice order_by: 
        :param bool desc: descending
    
        :return: void
        :rtype: void
        """
        self.from_ = from_
        self.to_ = to_
        self.order_by = order_by
        self.desc = desc
