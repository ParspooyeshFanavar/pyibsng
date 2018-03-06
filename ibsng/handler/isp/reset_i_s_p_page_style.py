"""Reset ISP page style API method."""
from ibsng.handler.handler import Handler


class resetISPPageStyle(Handler):
    """Reset ISP page style method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_id, int)

    def setup(self, isp_id):
        """Setup required parameters.

        :param int isp_id: isp id

        :return: None
        :rtype: None
        """
        self.isp_id = isp_id
