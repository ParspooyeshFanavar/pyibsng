"""Message Center info API method."""
from ibsng.handler.handler import Handler


class getProviderInfoByName(Handler):
    """Message Center info method class."""

    def setup(self, provider_name):
        """Setup required parameters.

        :param str provider_name: 
    
        :return: void
        :rtype: void
        """
        self.provider_name = provider_name
