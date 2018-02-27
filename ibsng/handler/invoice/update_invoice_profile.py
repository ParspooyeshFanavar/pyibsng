"""Update invoice profile API method."""
from ibsng.handler.handler import Handler


class updateInvoiceProfile(Handler):
    """Update invoice profile method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.profile_id, int)
        self.is_valid(self.profile_name, str)
        self.is_valid(self.isp_name, str, False)
        self.is_valid(self.rules, list, False)
        self.is_valid(self.comment, str, False)

    def setup(self, profile_id, profile_name,
              isp_name="", rules=[], comment=""):
        """Setup required parameters.

        :param int profile_id: profile id
        :param str profile_name: new profile name
        :param str isp_name: new isp name
        :param list rules: new rules
        :param str comment: new comment

        :return: None
        :rtype: None
        """
        self.profile_id = profile_id
        self.profile_name = profile_name
        self.isp_name = isp_name
        self.rules = rules
        self.comment = comment
