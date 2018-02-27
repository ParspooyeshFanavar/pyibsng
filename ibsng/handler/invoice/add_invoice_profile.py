"""Add invoice profile API method."""
from ibsng.handler.handler import Handler


class addInvoiceProfile(Handler):
    """Add invoice profile method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_name, str)
        self.is_valid(self.isp_name, str, False)
        self.is_valid(self.comment, str, False)

    def setup(self, profile_name, isp_name="", comment=""):
        """Setup required parameters.

        :param str profile_name: profile name
        :param str isp_name: isp name
        :param str comment: invoice comment

        :return: None
        :rtype: None
        """
        self.profile_name = profile_name
        self.isp_name = isp_name
        self.comment = comment
