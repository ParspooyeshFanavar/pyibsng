""" info API method."""
from ibsng.handler.handler import Handler


class deleteSavedReport(Handler):
    """ info method class."""

    def setup(self, report_auth, report_type, report_date, report_status, report_format):
        """Setup required parameters.

        :param str report_auth: admin username
        :param str report_type: 
        :param str report_date: format: YYYYMMDD
        :param choice report_status: 
        :param choice report_format: 
    
        :return: void
        :rtype: void
        """
        self.report_auth = report_auth
        self.report_type = report_type
        self.report_date = report_date
        self.report_status = report_status
        self.report_format = report_format
