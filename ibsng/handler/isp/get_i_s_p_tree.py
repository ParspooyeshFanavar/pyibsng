"""Get ISP tree API method."""
from ibsng.handler.handler import Handler


class getISPTree(Handler):
    """Get ISP tree method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.isp_name, str, False)

    def setup(self, isp_name=None):
        """Setup required parameters.

        :param str isp_name: isp name (if this param is missing, we use
                             admin's owner ISP)

        :return: None
        :rtype: None
        """
        self.isp_name = isp_name
