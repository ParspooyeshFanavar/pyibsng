"""Add new interface API method."""
from ibsng.handler.handler import Handler


class addInterface(Handler):
    """Add new interface class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.hostname, str)
        self.is_valid(self.interface_name, str)
        self.is_valid(self.host_type, str)
        self.is_valid_content(self.host_type, "(Linux|Mikrotik)")
        self.is_valid(self.comment, str, False)

    def setup(self, hostname, interface_name, host_type, comment=""):
        """Setup required parameters.

        :param str hostname: host name
        :param str interface_name: interface name
        :param str host_type: type of host (choice: Linux, Mikrotik)
        :param str comment: comment about this action

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.interface_name = interface_name
        self.host_type = host_type
        self.comment = comment
