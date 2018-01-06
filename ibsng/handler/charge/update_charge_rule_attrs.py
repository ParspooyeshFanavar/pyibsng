""" info API method."""
from ibsng.handler.handler import Handler


class updateChargeRuleAttrs(Handler):
    """ info method class."""

    def setup(self, charge_rule_id, charge_name, update_attrs, delete_attrs):
        """Setup required parameters.

        :param int charge_rule_id: 
        :param str charge_name: 
        :param dict update_attrs: 
        :param list delete_attrs: 
    
        :return: void
        :rtype: void
        """
        self.charge_rule_id = charge_rule_id
        self.charge_name = charge_name
        self.update_attrs = update_attrs
        self.delete_attrs = delete_attrs
