"""Get user info keys API method."""
from ibsng.handler.handler import Handler


class getUserInfoKeys(Handler):
    """Get user info keys method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.domain, str)

    def setup(self, domain_name):
        """Setup required parameters.

        :param str domain_name: name of ldap domain

        :return: None
        :rtype: None
        """
        self.domain = domain_name
