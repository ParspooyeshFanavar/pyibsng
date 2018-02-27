"""Set LDAP IBSng mapping API method."""
from ibsng.handler.handler import Handler


class setLDAPIBSMapping(Handler):
    """Set LDAP IBSng mapping method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.domain, str)
        self.is_valid(self.ldap_attribute, str)
        self.is_valid(self.IBS_field, str)
        self.is_valid(self.sync, bool)

    def setup(self, domain, ldap_attribute, ibsng_field, sync):
        """Setup required parameters.

        :param str domain: name of ldap domain in which mapping takes place
        :param str ldap_attribute: ldap side of attribute mapping
        :param str ibsng_field: ibs side of attribute mapping
        :param bool sync: specifies if the mapping be synchronized or not

        :return: None
        :rtype: None
        """
        self.domain = domain
        self.ldap_attribute = ldap_attribute
        self.IBS_field = ibsng_field
        self.sync = sync
