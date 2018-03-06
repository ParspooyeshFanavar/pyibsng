"""Delete load balancing ip pool API method."""
from ibsng.handler.handler import Handler


class deleteLoadBalancingIPpool(Handler):
    """Delete load balancing ip pool method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ippool_name, str)

    def setup(self, ippool_name):
        """Setup required parameters.

        :param str ippool_name: ip pool name

        :return: None
        :rtype: None
        """
        self.ippool_name = ippool_name
