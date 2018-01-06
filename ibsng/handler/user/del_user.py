""" info API method."""
from ibsng.handler.handler import Handler


class delUser(Handler):
    """ info method class."""

    def setup(self, user_id, delete_comment, del_connection_logs, del_audit_logs):
        """Setup required parameters.

        :param str user_id: comma-seperated User IDs
        :param str delete_comment: 
        :param bool del_connection_logs: pass true if you want users' connection logs to be deleted too
        :param bool del_audit_logs: pass true if you want users' audit logs to be deleted too
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.delete_comment = delete_comment
        self.del_connection_logs = del_connection_logs
        self.del_audit_logs = del_audit_logs
