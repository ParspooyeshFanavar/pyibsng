"""All LDAP methods info API method."""
from ibsng.handler.handler import Handler


class deleteLDAPIBSMapping(Handler):
    """All LDAP methods info method class."""

    def setup(self, domain, ldap_attribute, IBS_field, sync):
        """Setup required parameters.

        :param str domain: name of ldap domain in which mapping takes place
        :param str ldap_attribute: ldap side of attribute mapping
        :param str IBS_field: ibs side of attribute mapping
        :param bool sync: specifies if the mapping be synchronized or not
    
        :return: void
        :rtype: void
        """
        self.domain = domain
        self.ldap_attribute = ldap_attribute
        self.IBS_field = IBS_field
        self.sync = sync
