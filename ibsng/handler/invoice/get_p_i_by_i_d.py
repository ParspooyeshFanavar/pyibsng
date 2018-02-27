"""Get pi by id API method."""
from ibsng.handler.handler import Handler


class getPIByID(Handler):
    """Get pi by id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.pi_id, int)

    def setup(self, pi_id):
        """Setup required parameters.

        :param int pi_id: pi id

        :return: None
        :rtype: None
        """
        self.pi_id = pi_id
