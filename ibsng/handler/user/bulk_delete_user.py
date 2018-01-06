""" info API method."""
from ibsng.handler.handler import Handler


class bulkDeleteUser(Handler):
    """ info method class."""

    def setup(self, conds, delete_comment, del_connection_logs, del_audit_logs):
        """Setup required parameters.

        :param dict conds: the same as method 'user.searchUser', parameter 'conds'
        :param str delete_comment: the same as method 'user.delUser'
        :param bool del_connection_logs: the same as method 'user.delUser'
        :param bool del_audit_logs: the same as method 'user.delUser'
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.delete_comment = delete_comment
        self.del_connection_logs = del_connection_logs
        self.del_audit_logs = del_audit_logs
