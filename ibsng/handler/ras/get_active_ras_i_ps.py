"""Get active ras by ips API method."""
from ibsng.handler.handler import Handler


class getActiveRasIPs(Handler):
    """Get active ras by ips info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.type_filter, str)

    def setup(self, type_filter):
        """Setup required parameters.

        :param str type_filter: type filter

        :return: None
        :rtype: None
        """
        self.type_filter = type_filter
