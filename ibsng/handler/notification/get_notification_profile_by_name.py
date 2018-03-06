""" info API method."""
from ibsng.handler.handler import Handler


class getNotificationProfileByName(Handler):
    """ info method class."""

    def setup(self, notification_profile_name):
        """Setup required parameters.

        :param str notification_profile_name: 
    
        :return: void
        :rtype: void
        """
        self.notification_profile_name = notification_profile_name
