"""Delete ras API method."""
from ibsng.handler.handler import Handler


class deleteRas(Handler):
    """Delete ras method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ras_id, int)

    def setup(self, ras_id):
        """Setup required parameters.

        :param int ras_id: ras id

        :return: None
        :rtype: None
        """
        self.ras_id = ras_id
