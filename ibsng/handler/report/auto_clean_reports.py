""" info API method."""
from ibsng.handler.handler import Handler


class autoCleanReports(Handler):
    """ info method class."""

    def setup(self, connection_log_clean, connection_log_unit, credit_change_clean, credit_change_unit, user_audit_log_clean, user_audit_log_unit, snapshots_clean, snapshots_unit, bw_snapshots_clean, bw_snapshots_unit, web_analyzer_clean, web_analyzer_unit):
        """Setup required parameters.

        :param int connection_log_clean: period
        :param choice connection_log_unit: 
        :param int credit_change_clean: relative time
        :param choice credit_change_unit: relative time unit
        :param int user_audit_log_clean: relative time
        :param choice user_audit_log_unit: relative time unit
        :param int snapshots_clean: relative time
        :param choice snapshots_unit: relative time unit
        :param int bw_snapshots_clean: relative time
        :param choice bw_snapshots_unit: relative time unit
        :param int web_analyzer_clean: relative time
        :param choice web_analyzer_unit: relative time unit
    
        :return: void
        :rtype: void
        """
        self.connection_log_clean = connection_log_clean
        self.connection_log_unit = connection_log_unit
        self.credit_change_clean = credit_change_clean
        self.credit_change_unit = credit_change_unit
        self.user_audit_log_clean = user_audit_log_clean
        self.user_audit_log_unit = user_audit_log_unit
        self.snapshots_clean = snapshots_clean
        self.snapshots_unit = snapshots_unit
        self.bw_snapshots_clean = bw_snapshots_clean
        self.bw_snapshots_unit = bw_snapshots_unit
        self.web_analyzer_clean = web_analyzer_clean
        self.web_analyzer_unit = web_analyzer_unit
