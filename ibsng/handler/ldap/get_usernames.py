"""All LDAP methods info API method."""
from ibsng.handler.handler import Handler


class getUsernames(Handler):
    """All LDAP methods info method class."""

    def setup(self, starts_with):
        """Setup required parameters.

        :param str starts_with: 
    
        :return: void
        :rtype: void
        """
        self.starts_with = starts_with
