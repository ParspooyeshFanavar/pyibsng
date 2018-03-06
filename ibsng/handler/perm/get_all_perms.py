"""Get all permissions API method."""
from ibsng.handler.handler import Handler


class getAllPerms(Handler):
    """Get all permissions method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        if hasattr(self, 'category'):
            self.is_valid(self.category, str)

    def setup(self, category):
        """Setup required parameters.

        :param type category: category

        :return: None
        :rtype: None
        """
        if category:
            self.category = category
