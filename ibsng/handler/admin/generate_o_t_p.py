"""Generate OTP for an admin API method.

Generate one-time password for an admin.
"""
from ibsng.handler.handler import Handler


class generateOTP(Handler):
    """Generate OTP for an admin class."""

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
