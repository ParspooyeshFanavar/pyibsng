"""Multi string get all API method."""
from ibsng.handler.handler import Handler


class multiStrGetAll(Handler):
    """Multi string get all method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.str_, str)
        self.is_valid(self.left_pad, bool)

    def setup(self, string, left_pad):
        """Setup required parameters.

        :param str str: string
        :param bool left_pad: left pad

        :return: None
        :rtype: None
        """
        self.str_ = string
        self.left_pad = left_pad
