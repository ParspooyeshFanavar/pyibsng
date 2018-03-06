"""Message Center info API method."""
from ibsng.handler.handler import Handler


class adminSearchReceivedMessage(Handler):
    """Message Center info method class."""

    def setup(self, conds, from_index, to_index, order_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int from: page start index
        :param int to: page end index
        :param choice order_by: order by specific field
        :param bool desc: descending
    
        :return: None
        :rtype: None
        """
        self.conds = conds
        self.from_ = from_index
        self.to_ = to_index
        self.order_by = order_by
        self.desc = desc
