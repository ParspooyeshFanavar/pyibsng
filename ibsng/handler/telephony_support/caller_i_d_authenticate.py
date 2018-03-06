""" info API method."""
from ibsng.handler.handler import Handler


class callerIDAuthenticate(Handler):
    """ info method class."""

    def setup(self, caller_id):
        """Setup required parameters.

        :param str caller_id: 
    
        :return: void
        :rtype: void
        """
        self.caller_id = caller_id
