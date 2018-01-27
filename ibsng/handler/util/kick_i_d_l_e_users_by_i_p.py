"""Kick idle users by ip API method."""
from ibsng.handler.handler import Handler


class kickIDLEUsersByIP(Handler):
    """Kick idle users by ip method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.idle_ip_list, list)

    def setup(self, idle_ip_list):
        """Setup required parameters.

        :param list idle_ip_list: list of ip addresses

        :return: None
        :rtype: None
        """
        self.idle_ip_list = idle_ip_list
