"""Delete bandwidth static IP API method."""
from ibsng.handler.handler import Handler


class delBwStaticIP(Handler):
    """Delete bandwidth static IP class."""

    def setup(self, ip_addr):
        """Setup required parameters.

        :param str ip_addr: IP address

        :return: None
        :rtype: None
        """
        self.ip_addr = ip_addr
