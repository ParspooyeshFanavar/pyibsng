"""Get ISP info API method."""
from ibsng.handler.handler import Handler


class getISPInfo(Handler):
    """Get ISP info method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_name, str, False)
        self.is_valid(self.isp_id, int, False)

    def setup(self, isp_name=None, isp_id=None):
        """Setup required parameters.

        :param str isp_name: isp name
        :param int isp_id: isp id

        :return: None
        :rtype: None
        """
        self.isp_name = isp_name
        self.isp_id = isp_id
