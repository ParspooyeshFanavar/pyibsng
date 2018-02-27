"""Update attributes info API method."""
from ibsng.handler.handler import Handler


class updateAttributes(Handler):
    """Update attributes method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ras_ip, str)
        self.is_valid_content(self.ras_ip, self.IP_PATTERN)
        self.is_valid(self.attrs, dict)

    def setup(self, ras_ip, attrs):
        """Setup required parameters.

        :param str ras_ip: ras ip address
        :param dict attrs: ras attributes

        :return: None
        :rtype: None
        """
        self.ras_ip = ras_ip
        self.attrs = attrs
