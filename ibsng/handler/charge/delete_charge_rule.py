"""Delete charge rule API method."""
from ibsng.handler.handler import Handler


class deleteChargeRule(Handler):
    """Delete charge rule method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_rule_id, int)
        self.is_valid(self.charge_name, str)

    def setup(self, charge_rule_id, charge_name):
        """Setup required parameters.

        :param int charge_rule_id: charge rule id
        :param str charge_name: charge name

        :return: None
        :rtype: None
        """
        self.charge_rule_id = charge_rule_id
        self.charge_name = charge_name
