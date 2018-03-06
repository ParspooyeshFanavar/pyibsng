"""Change ISP deposit API method."""
from ibsng.handler.handler import Handler


class changeISPDeposit(Handler):
    """Change ISP deposit method class."""

    def control(self):
        """Validate inputs after method setup.

        :rtype: None
        :return: None
        """
        self.is_valid(self.isp_name, str)
        self.is_valid(self.deposit_amount, float)
        self.is_valid(self.comment, str)

    def setup(self, isp_name, deposit_amount, comment=""):
        """Setup required parameters.

        :param str isp_name: isp name
        :param float deposit_amount: deposit amount
        :param str comment: comment

        :return: None
        :rtype: None
        """
        self.isp_name = isp_name
        self.deposit_amount = deposit_amount
        self.comment = comment
