"""Message Center info API method."""
from ibsng.handler.handler import Handler


class checkActivationCode(Handler):
    """Message Center info method class."""

    def setup(self, activation_code):
        """Setup required parameters.

        :param str activation_code: 
    
        :return: void
        :rtype: void
        """
        self.activation_code = activation_code
