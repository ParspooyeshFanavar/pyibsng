"""All LDAP methods info API method."""
from ibsng.handler.handler import Handler


class setLDAPSearchOptionsByDomain(Handler):
    """All LDAP methods info method class."""

    def setup(self, domain, search_filter, search_base):
        """Setup required parameters.

        :param str domain: name of ldap domain to be queried
        :param str search_filter: ldap query search filter by which ldap users will be fetched
        :param str search_base: ldap query search base by which ldap users will be fetched
    
        :return: void
        :rtype: void
        """
        self.domain = domain
        self.search_filter = search_filter
        self.search_base = search_base
