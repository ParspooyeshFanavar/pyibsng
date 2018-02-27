"""Web login API method."""
from ibsng.handler.handler import Handler


class webLogin(Handler):
    """Web login method class."""

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
        self.is_valid(self.auth_remoteaddr, str)
        self.is_valid_content(self.auth_remoteaddr, self.IP_PATTERN)

    def setup(self, login_auth_type, login_auth_name,
              login_auth_pass, auth_remoteaddr):
        """Setup required parameters.

        :param str login_auth_type: authentication type
                                    ("ADMIN", "NORMAL_USER", "VOIP_USER")
        :param str login_auth_name: authentication username
        :param str login_auth_pass: authentication password
        :param str auth_remoteaddr: remote IP of requester(admin/user)

        :return: None
        :rtype: None
        """
        self.login_auth_type = login_auth_type
        self.login_auth_name = login_auth_name
        self.login_auth_pass = login_auth_pass
        self.auth_remoteaddr = auth_remoteaddr
