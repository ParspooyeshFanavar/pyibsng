"""Add new charge API method."""
from ibsng.handler.handler import Handler


class addNewCharge(Handler):
    """Add new charge info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_name, str)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.comment, str, False)

    def setup(self, charge_name, isp_name, comment=""):
        """Setup required parameters.

        :param str charge_name: charge name
        :param str isp_name: isp name
        :param str comment: charge comment

        :return: None
        :rtype: None
        """
        self.charge_name = charge_name
        self.isp_name = isp_name
        self.comment = comment
