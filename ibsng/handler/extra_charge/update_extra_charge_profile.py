""" info API method."""
from ibsng.handler.handler import Handler


class updateExtraChargeProfile(Handler):
    """ info method class."""

    def setup(self, profile_id, profile_name, comment, effective_hour, rules):
        """Setup required parameters.

        :param int profile_id: 
        :param str profile_name: 
        :param str comment: 
        :param str effective_hour: format: HH:MM
        :param list rules: 
    
        :return: void
        :rtype: void
        """
        self.profile_id = profile_id
        self.profile_name = profile_name
        self.comment = comment
        self.effective_hour = effective_hour
        self.rules = rules
