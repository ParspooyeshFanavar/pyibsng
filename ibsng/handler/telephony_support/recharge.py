""" info API method."""
from ibsng.handler.handler import Handler


class recharge(Handler):
    """ info method class."""

    def setup(self, user_id, pin):
        """Setup required parameters.

        :param int user_id: 
        :param str pin: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.pin = pin
