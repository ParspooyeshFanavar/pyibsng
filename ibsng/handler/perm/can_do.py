"""Can do info API method."""
from ibsng.handler.handler import Handler


class canDo(Handler):
    """Can do info method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.perm_name, str)
        self.is_valid(self.admin_username, str)
        self.is_valid(self.params, list)

    def setup(self, perm_name, admin_username, params):
        """Setup required parameters.

        :param str perm_name: permission name
        :param str admin_username: admin username
        :param list params: parameter list

        :return: None
        :rtype: None
        """
        self.perm_name = perm_name
        self.admin_username = admin_username
        self.params = params
