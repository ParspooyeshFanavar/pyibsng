"""List groups with id API method."""
from ibsng.handler.handler import Handler


class listGroupsWithIDs(Handler):
    """List groups with id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.active_only, bool)

    def setup(self, active_only=False):
        """Setup required parameters.

        :param bool active_only: pass true if you only want active groups

        :return: None
        :rtype: None
        """
        self.active_only = active_only
