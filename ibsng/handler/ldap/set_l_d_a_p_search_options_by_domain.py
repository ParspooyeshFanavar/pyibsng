"""Set LDAP search options by domain API method."""
from ibsng.handler.handler import Handler


class setLDAPSearchOptionsByDomain(Handler):
    """Set LDAP search options by domain method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.domain, str)
        self.is_valid(self.search_filter, str)
        self.is_valid(self.search_base, str)

    def setup(self, domain, search_filter, search_base):
        """Setup required parameters.

        :param str domain: name of ldap domain to be queried
        :param str search_filter: ldap query search filter by which ldap users
                                  will be fetched
        :param str search_base: ldap query search base by which ldap users
                                will be fetched

        :return: None
        :rtype: None
        """
        self.domain = domain
        self.search_filter = search_filter
        self.search_base = search_base
