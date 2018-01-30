"""Update charge API method."""
from ibsng.handler.handler import Handler


class updateCharge(Handler):
    """Update charge method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_id, int)
        self.is_valid(self.charge_name, str)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.comment, str, False)

    def setup(self, charge_id, charge_name, isp_name, comment=""):
        """Setup required parameters.

        :param int charge_id: charge id
        :param str charge_name: new charge name
        :param str isp_name: new isp name
        :param str comment: new charge comment

        :return: None
        :rtype: None
        """
        self.charge_id = charge_id
        self.charge_name = charge_name
        self.comment = comment
        self.isp_name = isp_name
