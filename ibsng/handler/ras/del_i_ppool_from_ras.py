"""Delete ippool from ras API method."""
from ibsng.handler.handler import Handler


class delIPpoolFromRas(Handler):
    """Delete ippool from ras method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ras_ip, str)
        self.is_valid_content(self.ras_ip, self.IP_PATTERN)
        self.is_valid(self.ippool_name, str)

    def setup(self, ras_ip, ippool_name):
        """Setup required parameters.

        :param str ras_ip: ras ip address
        :param str ippool_name: ippool name

        :return: None
        :rtype: None
        """
        self.ras_ip = ras_ip
        self.ippool_name = ippool_name
