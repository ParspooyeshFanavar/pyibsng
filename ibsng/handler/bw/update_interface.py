"""Update interface API method."""
from ibsng.handler.handler import Handler


class updateInterface(Handler):
    """Updat interface class."""

    def setup(self, interface_id, hostname, interface_name, comment, host_type):
        """Setup required parameters.

        :param int interface_id: interface ID
        :param str hostname: new host name
        :param str interface_name: new interface name
        :param str comment: comment about this action
        :param str host_type: new host type (Linux, Mikrotik)

        :return: None
        :rtype: None
        """
        self.interface_id = interface_id
        self.hostname = hostname
        self.interface_name = interface_name
        self.comment = comment
        self.host_type = host_type
