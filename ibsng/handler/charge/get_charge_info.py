"""Get charge info API method."""
from ibsng.handler.handler import Handler


class getChargeInfo(Handler):
    """Get charge info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        if getattr(self, "charge_name"):
            self.is_valid(self.charge_name, str)
        elif getattr(self, "charge_id"):
            self.is_valid(self.charge_id, int)

    def setup(self, charge_name, charge_id=None):
        """Setup required parameters.

        :param charge_name: charge name
        :type charge_name: str
        :param charge_id: charge id
        :type charge_id: int

        :return: None
        :rtype: None
        """
        if charge_name:
            self.charge_name = charge_name
        elif charge_id:
            self.charge_id = charge_id
