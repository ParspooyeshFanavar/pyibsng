"""Delete saved report API method."""
from ibsng.handler.handler import Handler


class deleteSavedReport(Handler):
    """Delete saved report method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.report_auth, str)
        self.is_valid(self.report_type, str)
        self.is_valid(self.report_date, str)
        self.is_valid(self.report_status, str)
        self.is_valid_content(self.report_status, "(started|finished)")
        self.is_valid(self.report_format, str)
        self.is_valid_content(self.report_format, "(csv|pdf)")

    def setup(self, report_auth, report_type,
              report_date, report_status, report_format):
        """Setup required parameters.

        :param str report_auth: admin username
        :param str report_type: report type
        :param str report_date: format: YYYYMMDD
        :param str report_status: report status (started, finished)
        :param str report_format: report format (csv, pdf)

        :return: None
        :rtype: None
        """
        self.report_auth = report_auth
        self.report_type = report_type
        self.report_date = report_date
        self.report_status = report_status
        self.report_format = report_format
