"""Get tree API method."""
from ibsng.handler.handler import Handler


class getTree(Handler):
    """Get tree class."""

    def setup(self, hostname, interface_name):
        """Setup required parameters.

        :param str hostname: host name
        :param str interface_name: interface name

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.interface_name = interface_name
