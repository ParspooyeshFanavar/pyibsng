""" info API method."""
from ibsng.handler.handler import Handler


class setFeshfesheParams(Handler):
    """ info method class."""

    def setup(self, user_id, traffic, date_from, date_to):
        """Setup required parameters.

        :param int user_id: 
        :param int traffic: Traffic, in Mega Bytes
        :param str_datetime date_from: start date and time, format '%Y-%m-%d %H:%M'
        :param str_datetime date_to: end date and time, format '%Y-%m-%d %H:%M'
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.traffic = traffic
        self.date_from = date_from
        self.date_to = date_to
