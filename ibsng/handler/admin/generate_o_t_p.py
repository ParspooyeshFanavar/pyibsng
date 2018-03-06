"""Generate OTP for an admin API method.

Generate one-time password for an admin.
"""
from ibsng.handler.handler import Handler


class generateOTP(Handler):
    """Generate OTP for an admin class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.pass_len, int)
        self.is_valid(self.pass_count, int)
        self.is_valid(self.admin_username, str)

    def setup(self, pass_len, pass_count, admin_username):
        """Setup required parameters.

        :param int pass_len: password length
        :param int pass_count: count of password
        :param str admin_username: admin authentication username

        :return: None
        :rtype: None
        """
        self.pass_len = pass_len
        self.pass_count = pass_count
        self.admin_username = admin_username
