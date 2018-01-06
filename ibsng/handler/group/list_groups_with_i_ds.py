""" info API method."""
from ibsng.handler.handler import Handler


class listGroupsWithIDs(Handler):
    """ info method class."""

    def setup(self, active_only=None):
        """Setup required parameters.

        :param bool active_only: pass true if you only want active groups
    
        :return: void
        :rtype: void
        """
        self.active_only = active_only
