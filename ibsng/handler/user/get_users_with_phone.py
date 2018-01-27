"""Get users by phone API method."""
from ibsng.handler.handler import Handler


class getUsersWithPhone(Handler):
    """Get users by phone method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.phone, str)

    def setup(self, phone):
        """Setup required parameters.

        :param str phone: ibsng users phone

        :return: None
        :rtype: None
        """
        self.phone = phone
