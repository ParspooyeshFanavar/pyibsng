"""Delete interface API method."""
from ibsng.handler.handler import Handler


class delInterface(Handler):
    """Delete interface class."""

    def setup(self, hostname, interface_name):
        """Setup required parameters.

        :param str hostname: host name
        :param str interface_name: interface name

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.interface_name = interface_name
