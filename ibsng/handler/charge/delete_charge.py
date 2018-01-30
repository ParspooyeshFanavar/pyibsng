"""Delete charge API method."""
from ibsng.handler.handler import Handler


class deleteCharge(Handler):
    """Delete charge method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_name, str)

    def setup(self, charge_name):
        """Setup required parameters.

        :param str charge_name: charge name

        :return: None
        :rtype: None
        """
        self.charge_name = charge_name
