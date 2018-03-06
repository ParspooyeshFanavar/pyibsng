"""Get active leaves API method."""
from ibsng.handler.handler import Handler


class getActiveLeaves(Handler):
    """Get active leaves class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.order_by, str)
        self.is_valid(self.desc, bool)

    def setup(self, order_by, desc):
        """Setup required parameters.

        :param str order_by: order by a specific field
        :param bool desc: order of result

        :return: None
        :rtype: None
        """
        self.order_by = order_by
        self.desc = desc
