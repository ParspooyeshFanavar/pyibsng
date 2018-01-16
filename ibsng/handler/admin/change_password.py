"""Admin change password API method."""
from ibsng.handler.handler import Handler


class changePassword(Handler):
    """Admin change password class."""

    def setup(self, admin_username, new_password):
        """Setup required parameters.

        :param str admin_username: admin authentication username 
        :param str new_password: admin authentication new password
 
        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
        self.new_password = new_password
