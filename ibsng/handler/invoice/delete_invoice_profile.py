"""Delete invoice profile API method."""
from ibsng.handler.handler import Handler


class deleteInvoiceProfile(Handler):
    """Delete invoice profile method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_id, str)

    def setup(self, profile_id):
        """Setup required parameters.

        :param int profile_id: profile id

        :return: None
        :rtype: None
        """
        self.profile_id = profile_id
