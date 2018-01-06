"""Message Center info API method."""
from ibsng.handler.handler import Handler


class addNewProvider(Handler):
    """Message Center info method class."""

    def setup(self, provider_type, provider_name, msg_type):
        """Setup required parameters.

        :param choice provider_type: 
        :param str provider_name: 
        :param choice msg_type: 
    
        :return: void
        :rtype: void
        """
        self.provider_type = provider_type
        self.provider_name = provider_name
        self.msg_type = msg_type
