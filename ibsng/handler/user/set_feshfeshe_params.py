"""Set Feshfeshe params API method."""
from ibsng.handler.handler import Handler


class setFeshfesheParams(Handler):
    """Set Feshfeshe params method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.traffic, float)
        self.is_valid(self.date_from, str)
        self.is_valid(self.date_to, str)

    def setup(self, user_id, traffic, date_from, date_to):
        """Setup required parameters.

        :param int user_id: ibsng user id
        :param int traffic: Traffic, in Mega Bytes
        :param str_datetime date_from: start date and time,
                                       format '%Y-%m-%d %H:%M'
        :param str_datetime date_to: end date and time,
                                     format '%Y-%m-%d %H:%M'

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.traffic = traffic
        self.date_from = date_from
        self.date_to = date_to
