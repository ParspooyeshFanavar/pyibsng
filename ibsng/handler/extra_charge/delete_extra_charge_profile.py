"""Delete extra charge profile API method."""
from ibsng.handler.handler import Handler


class deleteExtraChargeProfile(Handler):
    """Delete extra charge profile method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_name, str)

    def setup(self, profile_name):
        """Setup required parameters.

        :param str profile_name: profile name

        :return: None
        :rtype: None
        """
        self.profile_name = profile_name
