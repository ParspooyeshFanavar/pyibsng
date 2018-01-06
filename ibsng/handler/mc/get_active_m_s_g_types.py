"""Message Center info API method."""
from ibsng.handler.handler import Handler


class getActiveMSGTypes(Handler):
    """Message Center info method class."""

    def setup(self, view_type):
        """Setup required parameters.

        :param choice view_type: 
    
        :return: void
        :rtype: void
        """
        self.view_type = view_type
