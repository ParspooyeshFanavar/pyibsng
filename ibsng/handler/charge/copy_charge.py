"""Copy charge API method."""
from ibsng.handler.handler import Handler


class copyCharge(Handler):
    """Copy charge info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_name, str)
        self.is_valid(self.copy_count, int)
        self.is_valid(self.comment, str, False)

    def setup(self, charge_name, copy_count, comment=""):
        """Setup required parameters.

        :param str charge_name: charge name
        :param int copy_count: count of copy
        :param str comment: charge comment

        :return: None
        :rtype: None
        """
        self.charge_name = charge_name
        self.copy_count = copy_count
        self.comment = comment
