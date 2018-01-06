""" info API method."""
from ibsng.handler.handler import Handler


class changeNotificationStatus(Handler):
    """ info method class."""

    def setup(self, notification_id, read):
        """Setup required parameters.

        :param int notification_id: 
        :param bool read: 
    
        :return: void
        :rtype: void
        """
        self.notification_id = notification_id
        self.read = read
