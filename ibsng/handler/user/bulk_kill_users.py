"""Bulk action to kill user API method."""
from ibsng.handler.handler import Handler


class bulkKillUsers(Handler):
    """Bulk action to kill user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.kill, bool)

    def setup(self, conds, kill=False):
        """Setup required parameters.

        :param dict conds: conditions
        :param bool kill: True means 'Kill User', False means 'Clear User'

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.kill = kill
