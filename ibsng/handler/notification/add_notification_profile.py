""" info API method."""
from ibsng.handler.handler import Handler


class addNotificationProfile(Handler):
    """ info method class."""

    def setup(self, notification_profile_name, notification_profile_comment):
        """Setup required parameters.

        :param str notification_profile_name: 
        :param str notification_profile_comment: 
    
        :return: void
        :rtype: void
        """
        self.notification_profile_name = notification_profile_name
        self.notification_profile_comment = notification_profile_comment
