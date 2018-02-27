"""Login API method."""
from ibsng.handler.handler import Handler


class login(Handler):
    """Login method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.login_auth_type, str)
        self.is_valid_choice(self.login_auth_type,
                             ["ADMIN", "NORMAL_USER", "VOIP_USER"])
        self.is_valid(self.login_auth_name, str)
        self.is_valid(self.login_auth_pass, str)

    def setup(self, login_auth_type, login_auth_name, login_auth_pass):
        """Setup required parameters.

        :param str login_auth_type: authentication type
                                    ("ADMIN", "NORMAL_USER", "VOIP_USER")
        :param str login_auth_name: authentication username
        :param str login_auth_pass: authentication password

        :return: None
        :rtype: None
        """
        self.login_auth_type = login_auth_type
        self.login_auth_name = login_auth_name
        self.login_auth_pass = login_auth_pass
