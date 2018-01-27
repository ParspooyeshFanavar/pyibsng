"""Get system notification API method."""
from ibsng.handler.handler import Handler


class getNotifications(Handler):
    """Get system notification method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.last_notifications, int)
        self.is_valid_content(self.last_notifications, self.POSITIVE_NUMBER)
        self.is_valid(self.only_unread, bool)

    def setup(self, last_notifications=5, only_unread=False):
        """Setup required parameters.

        :param int last_notifications: last notifications (default is 5)
        :param bool only_unread: just get unread notification

        :return: None
        :rtype: None
        """
        self.last_notifications = last_notifications
        self.only_unread = only_unread
