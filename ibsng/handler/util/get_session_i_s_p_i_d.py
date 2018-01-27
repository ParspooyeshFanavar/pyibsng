"""Get session isp id API method."""
from ibsng.handler.handler import Handler


class getSessionISPID(Handler):
    """Get session isp id method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.web_domain, str)

    def setup(self, web_domain):
        """Setup required parameters.

        :param str web_domain: domain of user/admin panel page

        :return: None
        :rtype: None
        """
        self.web_domain = web_domain
