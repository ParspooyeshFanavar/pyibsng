"""Message Center info API method."""
from ibsng.handler.handler import Handler


class adminEnqueueSend(Handler):
    """Message Center info method class."""

    def setup(self, body, destinations, msg_type, schedule_date, schedule_date_unit=None):
        """Setup required parameters.

        :param str body: 
        :param str destinations: comma-seperated list of destinations
        :param choice msg_type: 
        :param str_datetime, float schedule_date: 
        :param choice schedule_date_unit: 
    
        :return: void
        :rtype: void
        """
        self.body = body
        self.destinations = destinations
        self.msg_type = msg_type
        self.schedule_date = schedule_date
        self.schedule_date_unit = schedule_date_unit
