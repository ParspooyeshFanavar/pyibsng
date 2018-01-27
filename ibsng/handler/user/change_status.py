"""Change user status API method."""
from ibsng.handler.handler import Handler


class changeStatus(Handler):
    """Change user status method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.status, str)

    def setup(self, user_id, status):
        """Setup required parameters.

        :param str user_id: ibsng user id
        :param str status: new user status (Package, Recharged,
                           Temporary Extended)

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.status = status
