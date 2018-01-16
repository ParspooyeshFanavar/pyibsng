"""Add new interface API method."""
from ibsng.handler.handler import Handler


class addInterface(Handler):
    """Add new interface class."""

    def setup(self, hostname, interface_name, comment, host_type):
        """Setup required parameters.

        :param str hostname: host name 
        :param str interface_name: interface name
        :param str comment: comment about this action
        :param str host_type: type of host (choice: Linux, Mikrotik)

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.interface_name = interface_name
        self.comment = comment
        self.host_type = host_type
