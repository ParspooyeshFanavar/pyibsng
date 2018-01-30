"""Update change rule API method."""
from ibsng.handler.handler import Handler


class updateChargeRule(Handler):
    """Update charge rule method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_rule_id, int)
        self.is_valid(self.charge_rule_description, str, False)
        self.is_valid(self.charge_rule_priority, int)
        self.is_valid(self.charge_name, str)

    def setup(self, charge_rule_id, charge_rule_description,
              charge_rule_priority, charge_name):
        """Setup required parameters.

        :param int charge_rule_id: charge rule id
        :param str charge_rule_description: new charge rule description
        :param int charge_rule_priority: new charge rule priority
        :param str charge_name: new charge name

        :return: None
        :rtype: None
        """
        self.charge_rule_id = charge_rule_id
        self.charge_rule_description = charge_rule_description
        self.charge_rule_priority = charge_rule_priority
        self.charge_name = charge_name
