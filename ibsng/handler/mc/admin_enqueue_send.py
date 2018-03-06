"""Message Center info API method."""
from ibsng.handler.handler import Handler


class adminEnqueueSend(Handler):
    """Message Center info method class."""

    def setup(self, body, destinations, msg_type,
              schedule_date, schedule_date_unit=None):
        """Setup required parameters.

        :param str body: body string
        :param str destinations: comma-seperated list of destinations
        :param str msg_type: message type
        :param str schedule_date: send schedule date
        :param str schedule_date_unit: schedule date time

        :return: None
        :rtype: None
        """
        self.body = body
        self.destinations = destinations
        self.msg_type = msg_type
        self.schedule_date = schedule_date
        self.schedule_date_unit = schedule_date_unit
