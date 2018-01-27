"""Bulk action to renew user API method."""
from ibsng.handler.handler import Handler


class bulkRenewUsers(Handler):
    """Bulk action to renew user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.renew_comment, str, False)

    def setup(self, conds, renew_comment=""):
        """Setup required parameters.

        :param dict conds: conditions
        :param str renew_comment: comment for this action

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.renew_comment = renew_comment
