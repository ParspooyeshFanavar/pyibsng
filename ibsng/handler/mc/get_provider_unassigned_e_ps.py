"""Message Center info API method."""
from ibsng.handler.handler import Handler


class getProviderUnassignedEPs(Handler):
    """Message Center info method class."""

    def setup(self, provider_name, count, starts_with):
        """Setup required parameters.

        :param str provider_name: 
        :param int count: 
        :param str starts_with: 
    
        :return: void
        :rtype: void
        """
        self.provider_name = provider_name
        self.count = count
        self.starts_with = starts_with
