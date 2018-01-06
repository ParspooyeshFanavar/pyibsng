""" info API method."""
from ibsng.handler.handler import Handler


class deleteChargeRule(Handler):
    """ info method class."""

    def setup(self, charge_rule_id, charge_name):
        """Setup required parameters.

        :param int charge_rule_id: 
        :param str charge_name: 
    
        :return: void
        :rtype: void
        """
        self.charge_rule_id = charge_rule_id
        self.charge_name = charge_name
