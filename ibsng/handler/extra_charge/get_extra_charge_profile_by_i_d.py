"""Get extra charge profile by id API method."""
from ibsng.handler.handler import Handler


class getExtraChargeProfileByID(Handler):
    """Get extra charge profile by id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_id, int)

    def setup(self, profile_id):
        """Setup required parameters.

        :param int profile_id: profile id

        :return: None
        :rtype: None
        """
        self.profile_id = profile_id
