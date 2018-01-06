""" info API method."""
from ibsng.handler.handler import Handler


class updateNotificationRule(Handler):
    """ info method class."""

    def setup(self, notification_rule_id, notification_profile_id, notification_type, notification_threshold, message_type, message_template):
        """Setup required parameters.

        :param int notification_rule_id: 
        :param int notification_profile_id: 
        :param choice notification_type: 
        :param float notification_threshold: 
        :param choice message_type: 
        :param str message_template: 
    
        :return: void
        :rtype: void
        """
        self.notification_rule_id = notification_rule_id
        self.notification_profile_id = notification_profile_id
        self.notification_type = notification_type
        self.notification_threshold = notification_threshold
        self.message_type = message_type
        self.message_template = message_template
