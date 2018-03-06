"""Update ip pool API method."""
from ibsng.handler.handler import Handler


class updateIPpool(Handler):
    """Update ip pool method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ippool_id, int)
        self.is_valid(self.ippool_name, str)
        self.is_valid(self.comment, str)

    def setup(self, ippool_id, ippool_name, comment):
        """Setup required parameters.

        :param int ippool_id: ip pool id
        :param str ippool_name: ip pool name
        :param str comment: ip pool comment

        :return: None
        :rtype: None
        """
        self.ippool_id = ippool_id
        self.ippool_name = ippool_name
        self.comment = comment
