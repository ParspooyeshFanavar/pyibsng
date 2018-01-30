"""List charges API method."""
from ibsng.handler.handler import Handler


class listCharges(Handler):
    """List charges method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_id, int)

    def setup(self, isp_id):
        """Setup required parameters.

        :param str isp_id: comma-seprated. list of isp ids

        :return: None
        :rtype: None
        """
        self.isp_id = isp_id
