""" info API method."""
from ibsng.handler.handler import Handler


class addNewChargeRule(Handler):
    """ info method class."""

    def setup(self, charge_rule_description, charge_rule_priority, charge_name):
        """Setup required parameters.

        :param str charge_rule_description: 
        :param int charge_rule_priority: 
        :param str charge_name: 
    
        :return: void
        :rtype: void
        """
        self.charge_rule_description = charge_rule_description
        self.charge_rule_priority = charge_rule_priority
        self.charge_name = charge_name
