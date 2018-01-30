"""Update charge rule attributes API method."""
from ibsng.handler.handler import Handler


class updateChargeRuleAttrs(Handler):
    """Update charge rule attributes method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_rule_id, int)
        self.is_valid(self.charge_name, str)
        self.is_valid(self.update_attrs, dict, False)
        self.is_valid(self.delete_attrs, list, False)

    def setup(self, charge_rule_id, charge_name,
              update_attrs={}, delete_attrs=[]):
        """Setup required parameters.

        :param int charge_rule_id: charge rule id
        :param str charge_name: charge name
        :param dict update_attrs: updated attributes. structure:
                                  {attribute_name: attribute_value}
        :param list delete_attrs: deleted attributes

        :return: None
        :rtype: None
        """
        self.charge_rule_id = charge_rule_id
        self.charge_name = charge_name
        self.update_attrs = update_attrs
        self.delete_attrs = delete_attrs
