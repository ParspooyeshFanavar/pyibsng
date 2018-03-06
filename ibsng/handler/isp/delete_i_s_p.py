"""Delete ISP API method."""
from ibsng.handler.handler import Handler


class deleteISP(Handler):
    """Delete ISP method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_name, str)

    def setup(self, isp_name):
        """Setup required parameters.

        :param str isp_name: isp name

        :return: None
        :rtype: None
        """
        self.isp_name = isp_name
