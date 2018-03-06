"""Add IPto pool API method."""
from ibsng.handler.handler import Handler


class addIPtoPool(Handler):
    """Add IPto pool method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ippool_name, str)
        self.is_valid(self.ip, str)

    def setup(self, ippool_name, ip):
        """Setup required parameters.

        :param str ippool_name: ip pool name
        :param str ip: ip address

        :return: None
        :rtype: None
        """
        self.ippool_name = ippool_name
        self.ip = ip
