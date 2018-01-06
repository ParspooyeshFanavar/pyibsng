"""Message Center info API method."""
from ibsng.handler.handler import Handler


class updateProviderAttrs(Handler):
    """Message Center info method class."""

    def setup(self, provider_name, to_update_attrs):
        """Setup required parameters.

        :param str provider_name: 
        :param dict to_update_attrs: 
    
        :return: void
        :rtype: void
        """
        self.provider_name = provider_name
        self.to_update_attrs = to_update_attrs
