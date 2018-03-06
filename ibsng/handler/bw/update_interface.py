"""Update interface API method."""
from ibsng.handler.handler import Handler


class updateInterface(Handler):
    """Updat interface class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.interface_id, int)
        self.is_valid_content(self.interface_id, self.ID_PATTERN)
        self.is_valid(self.hostname, str)
        self.is_valid(self.interface_name, str)
        self.is_valid(self.host_type, str)
        self.is_valid_content(self.host_type, "(Linux|Mikrotik)")
        self.is_valid(self.comment, str, False)

    def setup(self, interface_id, hostname,
              interface_name, host_type, comment=""):
        """Setup required parameters.

        :param int interface_id: interface id
        :param str hostname: new host name
        :param str interface_name: new interface name
        :param str host_type: new host type (Linux, Mikrotik)
        :param str comment: comment about this action

        :return: None
        :rtype: None
        """
        self.interface_id = interface_id
        self.hostname = hostname
        self.interface_name = interface_name
        self.host_type = host_type
        self.comment = comment
