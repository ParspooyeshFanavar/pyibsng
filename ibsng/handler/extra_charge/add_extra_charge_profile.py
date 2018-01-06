""" info API method."""
from ibsng.handler.handler import Handler


class addExtraChargeProfile(Handler):
    """ info method class."""

    def setup(self, profile_name, comment, effective_hour, rules):
        """Setup required parameters.

        :param str profile_name: 
        :param str comment: 
        :param str effective_hour: format: HH:MM
        :param list rules: 
    
        :return: void
        :rtype: void
        """
        self.profile_name = profile_name
        self.comment = comment
        self.effective_hour = effective_hour
        self.rules = rules
