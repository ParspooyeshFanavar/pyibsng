"""Update extra charge API method."""
from ibsng.handler.handler import Handler


class updateExtraChargeProfile(Handler):
    """Update extra charge method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_id, int)
        self.is_valid(self.profile_name, str)
        self.is_valid(self.effective_hour, str)
        self.is_valid(self.rules, list)
        self.is_valid(self.comment, str, False)

    def setup(self, profile_id, profile_name,
              effective_hour, rules, comment=""):
        """Setup required parameters.

        :param int profile_id: profile id
        :param str profile_name: new profile name
        :param str effective_hour: new effective hour (format: HH:MM)
        :param list rules: new rules list
        :param str comment: new extra charge comment

        :return: None
        :rtype: None
        """
        self.profile_id = profile_id
        self.profile_name = profile_name
        self.effective_hour = effective_hour
        self.rules = rules
        self.comment = comment
