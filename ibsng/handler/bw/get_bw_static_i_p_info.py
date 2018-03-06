"""Get bandwidth static IP info API method."""
from ibsng.handler.handler import Handler


class getBwStaticIPInfo(Handler):
    """Get bandwidth static IP info class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ip_addr, str)
        self.is_valid_content(self.ip_addr, self.IP_PATTERN)

    def setup(self, ip_addr):
        """Setup required parameters.

        :param str ip_addr: IP address

        :return: None
        :rtype: None
        """
        self.ip_addr = ip_addr
