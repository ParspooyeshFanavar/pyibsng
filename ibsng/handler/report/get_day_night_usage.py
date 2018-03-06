""" info API method."""
from ibsng.handler.handler import Handler


class getDayNightUsage(Handler):
    """ info method class."""

    def setup(self, start_date, end_date, nightly_charge_rule_ids):
        """Setup required parameters.

        :param str start_date: gregorian date, format '%Y-%m-%d'
        :param str end_date: gregorian date, format '%Y-%m-%d'
        :param list nightly_charge_rule_ids: list of Charge Rule IDs that are Nightly (Free)
    
        :return: void
        :rtype: void
        """
        self.start_date = start_date
        self.end_date = end_date
        self.nightly_charge_rule_ids = nightly_charge_rule_ids
