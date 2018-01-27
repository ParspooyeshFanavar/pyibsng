"""Clear bulk action API method."""
from ibsng.handler.handler import Handler


class clearBulkAction(Handler):
    """Clear bulk action method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.action_id, int)

    def setup(self, action_id):
        """Setup required parameters.

        :param str action_id: bulk action id

        :return: None
        :rtype: None
        """
        self.action_id = action_id
