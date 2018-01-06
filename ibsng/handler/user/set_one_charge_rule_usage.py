""" info API method."""
from ibsng.handler.handler import Handler


class setOneChargeRuleUsage(Handler):
    """ info method class."""

    def setup(self, user_id, charge_rule_id, credit_usage, time_usage, traffic_usage):
        """Setup required parameters.

        :param int user_id: 
        :param int charge_rule_id: 
        :param int credit_usage: pass 0 if you want to reset
        :param int time_usage: in seconds, pass 0 if you want to reset
        :param int traffic_usage: in bytes, pass 0 if you want to reset
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.charge_rule_id = charge_rule_id
        self.credit_usage = credit_usage
        self.time_usage = time_usage
        self.traffic_usage = traffic_usage
