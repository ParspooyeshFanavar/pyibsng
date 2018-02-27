"""Get invoice profile by userid API method."""
from ibsng.handler.handler import Handler


class getInvoiceProfileByUserID(Handler):
    """Get invoice profile by user id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)

    def setup(self, user_id):
        """Setup required parameters.

        :param int user_id: ibsng user id

        :return: None
        :rtype: None
        """
        self.user_id = user_id
