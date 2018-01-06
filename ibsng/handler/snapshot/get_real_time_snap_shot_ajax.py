"""Realtime snapshot API method."""
from ibsng.handler.handler import Handler


class getRealTimeSnapShotAjax(Handler):
    """Realtime snapshot method."""

    def setup(self, name, from_, from_unit, ras_ips='', date_type='jalali'):
        """Setup required parameters.

        :param str name: name
        :param int from_: from as hour
        :param str unit: unit ex: hours

        :return: void
        :rtype: void
        """
        self.name = name
        self.from_ = from_
        self.from_unit = from_unit
        self.ras_ips = ras_ips
        self.date_type = date_type
