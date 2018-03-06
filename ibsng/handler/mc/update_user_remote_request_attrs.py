"""Message Center info API method."""
from ibsng.handler.handler import Handler


class updateUserRemoteRequestAttrs(Handler):
    """Message Center info method class."""

    def setup(self, remote_report_status, remote_report_command, allowed_requesters, attrs):
        """Setup required parameters.

        :param str remote_report_status: 
        :param str remote_report_command: 
        :param str allowed_requesters: 
        :param dict attrs: 
    
        :return: void
        :rtype: void
        """
        self.remote_report_status = remote_report_status
        self.remote_report_command = remote_report_command
        self.allowed_requesters = allowed_requesters
        self.attrs = attrs
