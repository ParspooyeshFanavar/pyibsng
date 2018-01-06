""" info API method."""
from ibsng.handler.handler import Handler


class updateChargeRule(Handler):
    """ info method class."""

    def setup(self, charge_rule_id, charge_rule_description, charge_rule_priority, charge_name):
        """Setup required parameters.

        :param int charge_rule_id: 
        :param str charge_rule_description: 
        :param int charge_rule_priority: 
        :param str charge_name: str
    
        :return: void
        :rtype: void
        """
        self.charge_rule_id = charge_rule_id
        self.charge_rule_description = charge_rule_description
        self.charge_rule_priority = charge_rule_priority
        self.charge_name = charge_name
