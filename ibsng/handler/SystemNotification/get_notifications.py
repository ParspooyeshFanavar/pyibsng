""" info API method."""
from ibsng.handler.handler import Handler


class getNotifications(Handler):
    """ info method class."""

    def setup(self, last_notifications=None, only_unread=None):
        """Setup required parameters.

        :param int last_notifications: default is 5
        :param bool only_unread: default is false
    
        :return: void
        :rtype: void
        """
        self.last_notifications = last_notifications
        self.only_unread = only_unread
