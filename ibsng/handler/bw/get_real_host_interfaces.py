"""Get real host interfaces API method."""
from ibsng.handler.handler import Handler


class getRealHostInterfaces(Handler):
    """Get real host interfaces class."""

    def setup(self, hostname, host_type):
        """Setup required parameters.

        :param str hostname: host name
        :param str host_type: host type(Linux, Mikrotik)

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.host_type = host_type
