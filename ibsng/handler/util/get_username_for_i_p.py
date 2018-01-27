"""Get username for ip API method."""
from ibsng.handler.handler import Handler


class getUsernameForIP(Handler):
    """Get username for ip method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ip, str)
        self.is_valid_content(self.ip, self.IP_PATTERN)

    def setup(self, ip_address):
        """Setup required parameters.

        :param str ip: ip address

        :return: None
        :rtype: None
        """
        self.ip = ip_address
