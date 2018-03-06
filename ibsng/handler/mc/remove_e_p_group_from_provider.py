"""Message Center info API method."""
from ibsng.handler.handler import Handler


class removeEPGroupFromProvider(Handler):
    """Message Center info method class."""

    def setup(self, provider_id, end_point_group_id):
        """Setup required parameters.

        :param int provider_id: 
        :param int end_point_group_id: 
    
        :return: void
        :rtype: void
        """
        self.provider_id = provider_id
        self.end_point_group_id = end_point_group_id
