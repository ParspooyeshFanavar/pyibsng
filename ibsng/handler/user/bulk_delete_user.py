"""Bulk action to delete user API method."""
from ibsng.handler.handler import Handler


class bulkDeleteUser(Handler):
    """Bulk action to delte user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.delete_comment, str)
        self.is_valid(self.del_connection_logs, bool)
        self.is_valid(self.del_audit_logs, bool)

    def setup(self, conds, delete_comment, del_connection_logs, del_audit_logs):
        """Setup required parameters.

        :param dict conds: conditions
        :param str delete_comment: set comment for this action
        :param bool del_connection_logs: delete user connection logs
        :param bool del_audit_logs: delete user audit logs

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.delete_comment = delete_comment
        self.del_connection_logs = del_connection_logs
        self.del_audit_logs = del_audit_logs