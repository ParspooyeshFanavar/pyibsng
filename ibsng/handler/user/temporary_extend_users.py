""" info API method."""
from ibsng.handler.handler import Handler


class temporaryExtendUsers(Handler):
    """ info method class."""

    def setup(self, user_id, temporary_extend_hours, temporary_extend_credit):
        """Setup required parameters.

        :param str user_id: 
        :param int temporary_extend_hours: hours
        :param float temporary_extend_credit: credit
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.temporary_extend_hours = temporary_extend_hours
        self.temporary_extend_credit = temporary_extend_credit
