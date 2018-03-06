"""Load permissions from another admin API method."""
from ibsng.handler.handler import Handler


class loadPermsFromAnotherAdmin(Handler):
    """Load permissions from another admin method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)
        self.is_valid(self.load_from_admin_username, str)

    def setup(self, admin_username, load_from_admin_username):
        """Setup required parameters.

        :param str admin_username: admin username
        :param str load_from_admin_username: load from admin username

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
        self.load_from_admin_username = load_from_admin_username
