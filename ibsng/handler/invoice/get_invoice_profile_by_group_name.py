"""Get invoice profile by group name API method."""
from ibsng.handler.handler import Handler


class getInvoiceProfileByGroupName(Handler):
    """Get invoice profile by group name method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_name, str)

    def setup(self, group_name):
        """Setup required parameters.

        :param str group_name: ibsng group name

        :return: None
        :rtype: None
        """
        self.group_name = group_name
