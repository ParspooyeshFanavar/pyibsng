"""Add extra charge API method."""
from ibsng.handler.handler import Handler


class addExtraChargeProfile(Handler):
    """Add extra charge method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_name, str)
        self.is_valid(self.effective_hour, str)
        self.is_valid(self.rules, list)
        self.is_valid(self.comment, str, False)

    def setup(self, profile_name, effective_hour, rules, comment=""):
        """Setup required parameters.

        :param str profile_name: profile name
        :param str effective_hour: effective hour (format: HH:MM)
        :param list rules: rules list
        :param str comment: extra charge comment

        :return: None
        :rtype: None
        """
        self.profile_name = profile_name
        self.effective_hour = effective_hour
        self.rules = rules
        self.comment = comment
