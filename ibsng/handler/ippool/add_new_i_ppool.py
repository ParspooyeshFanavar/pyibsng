"""Add new ip pool API method."""
from ibsng.handler.handler import Handler


class addNewIPpool(Handler):
    """Add new ip pool method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ippool_name, str)
        self.is_valid(self.comment, str)

    def setup(self, ippool_name, comment):
        """Setup required parameters.

        :param str ippool_name: ip pool name
        :param str comment: comment

        :return: None
        :rtype: None
        """
        self.ippool_name = ippool_name
        self.comment = comment
