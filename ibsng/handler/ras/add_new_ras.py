"""Add new ras API method."""
from ibsng.handler.handler import Handler


class addNewRas(Handler):
    """Add new ras method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ras_ip, str)
        self.is_valid_content(self.ras_ip, self.IP_PATTERN)
        self.is_valid(self.ras_type, str)
        self.is_valid(self.radius_secret, str)
        self.is_valid(self.ras_description, str)
        self.is_valid(self.comment, str, False)

    def setup(self, ras_ip, ras_type,
              radius_secret, ras_description, comment=""):
        """Setup required parameters.

        :param str ras_ip: ras ip address
        :param str ras_type: ras type (get from ras.getRasTypes method)
        :param str radius_secret: radius secret code
        :param str ras_description: ras description
        :param str comment: comment

        :return: None
        :rtype: None
        """
        self.ras_ip = ras_ip
        self.ras_type = ras_type
        self.radius_secret = radius_secret
        self.ras_description = ras_description
        self.comment = comment
