"""Set charge rule usage API method."""
from ibsng.handler.handler import Handler


class setOneChargeRuleUsage(Handler):
    """Set charge rule usage method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.charge_rule_id, int)
        self.is_valid(self.credit_usage, int)
        self.is_valid(self.time_usage, int)
        self.is_valid(self.traffic_usage, int)

    def setup(self, user_id, charge_rule_id, credit_usage,
              time_usage, traffic_usage):
        """Setup required parameters.

        :param int user_id: ibsng user id
        :param int charge_rule_id: charge rule id
        :param int credit_usage: pass 0 if you want to reset
        :param int time_usage: in seconds, pass 0 if you want to reset
        :param int traffic_usage: in bytes, pass 0 if you want to reset

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.charge_rule_id = charge_rule_id
        self.credit_usage = credit_usage
        self.time_usage = time_usage
        self.traffic_usage = traffic_usage
