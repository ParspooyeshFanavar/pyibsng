"""All LDAP methods info API method."""
from ibsng.handler.handler import Handler


class getLDAPIBSMapping(Handler):
    """All LDAP methods info method class."""

    def setup(self, domain):
        """Setup required parameters.

        :param str domain: 
    
        :return: void
        :rtype: void
        """
        self.domain = domain
