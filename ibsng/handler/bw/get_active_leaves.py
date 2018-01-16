"""Get active leaves API method."""
from ibsng.handler.handler import Handler


class getActiveLeaves(Handler):
    """Get active leaves class."""

    def setup(self, order_by, desc):
        """Setup required parameters.

        :param str order_by: order by a specific field
        :param bool desc: order of result

        :return: None
        :rtype: None
        """
        self.order_by = order_by
        self.desc = desc
