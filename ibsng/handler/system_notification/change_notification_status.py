"""Change notification status API method."""
from ibsng.handler.handler import Handler


class changeNotificationStatus(Handler):
    """Change notification status method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.notification_id, int)
        self.is_valid_content(self.notification_id, self.ID_PATTERN)
        self.is_valid(self.read, bool)

    def setup(self, notification_id, read):
        """Setup required parameters.

        :param int notification_id: ibsng notification id
        :param bool read: change notification 'read' status

        :return: None
        :rtype: None
        """
        self.notification_id = notification_id
        self.read = read
