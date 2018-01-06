"""Message Center info API method."""
from ibsng.handler.handler import Handler


class addNewEPGroupToProvider(Handler):
    """Message Center info method class."""

    def setup(self, end_point_range, provider_name):
        """Setup required parameters.

        :param str end_point_range: comma-seperated end-point groups
        :param str provider_name: 
    
        :return: void
        :rtype: void
        """
        self.end_point_range = end_point_range
        self.provider_name = provider_name
