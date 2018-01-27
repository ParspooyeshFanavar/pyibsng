"""Delete user API method."""
from ibsng.handler.handler import Handler


class delUser(Handler):
    """Delete user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, str)
        self.is_valid(self.del_connection_logs, bool)
        self.is_valid(self.del_audit_logs, bool)
        self.is_valid(self.delete_comment, str, False)

    def setup(self, user_ids, del_connection_logs,
              del_audit_logs, delete_comment=""):
        """Setup required parameters.

        :param list user_id: list of ibsng user ids
        :param str delete_comment: comment for this action
        :param bool del_connection_logs: pass true if you want users'
                                         connection logs to be deleted too
        :param bool del_audit_logs: pass true if you want users' audit logs to
                                    be deleted too

        :return: None
        :rtype: None
        """
        self.user_id = ",".join(map(str, user_ids))
        self.del_connection_logs = del_connection_logs
        self.del_audit_logs = del_audit_logs
        self.delete_comment = delete_comment
