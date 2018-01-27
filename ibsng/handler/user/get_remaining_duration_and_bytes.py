"""Get remain duration and bytes API method."""
from ibsng.handler.handler import Handler


class getRemainingDurationAndBytes(Handler):
    """Get remain duration and bytes method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        if hasattr(self, "user_id"):
            self.is_valid(self.user_id, int)

    def setup(self, user_id=None):
        """Setup required parameters.

        :param int user_id: ibsng user id

        :return: None
        :rtype: None
        """
        if user_id:
            self.user_id = user_id
