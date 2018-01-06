"""Message Center info API method."""
from ibsng.handler.handler import Handler


class unAssingAllFromGroup(Handler):
    """Message Center info method class."""

    def setup(self, provider_name, end_point_group_id):
        """Setup required parameters.

        :param str provider_name: 
        :param int end_point_group_id: 
    
        :return: void
        :rtype: void
        """
        self.provider_name = provider_name
        self.end_point_group_id = end_point_group_id
