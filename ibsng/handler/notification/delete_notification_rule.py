""" info API method."""
from ibsng.handler.handler import Handler


class deleteNotificationRule(Handler):
    """ info method class."""

    def setup(self, notification_profile_id, notification_rule_id):
        """Setup required parameters.

        :param int notification_profile_id: 
        :param int notification_rule_id: 
    
        :return: void
        :rtype: void
        """
        self.notification_profile_id = notification_profile_id
        self.notification_rule_id = notification_rule_id
