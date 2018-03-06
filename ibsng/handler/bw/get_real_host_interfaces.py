"""Get real host interfaces API method."""
from ibsng.handler.handler import Handler


class getRealHostInterfaces(Handler):
    """Get real host interfaces class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.hostname, str)
        self.is_valid(self.host_type, str)
        self.is_valid_content(self.host_type, "(Linux|Mikrotik)")

    def setup(self, hostname, host_type):
        """Setup required parameters.

        :param str hostname: host name
        :param str host_type: host type(Linux, Mikrotik)

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.host_type = host_type
