"""Message Center info API method."""
from ibsng.handler.handler import Handler


class getEPGroupUsageInfo(Handler):
    """Message Center info method class."""

    def setup(self, end_point_group_id, provider_id):
        """Setup required parameters.

        :param int end_point_group_id: 
        :param int provider_id: 
    
        :return: void
        :rtype: void
        """
        self.end_point_group_id = end_point_group_id
        self.provider_id = provider_id
