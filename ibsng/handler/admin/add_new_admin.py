"""Add new admin API method."""
from ibsng.handler.handler import Handler


class addNewAdmin(Handler):
    """Add new admin class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_username, str)
        self.is_valid(self.admin_password, str)
        self.is_valid(self.admin_isp_name, str)
        self.is_valid(self.name, str)
        self.is_valid(self.email, str)
        self.is_valid_content(self.email, self.EMAIL_PATTERN)
        self.is_valid(self.comment, str, False)
        self.is_valid(self.admin_has_otp, bool)
        self.is_valid(self.admin_request_limit, int)

    def setup(self, admin_username, admin_password, admin_isp_name, name,
              email, comment, admin_has_otp, admin_request_limit):
        """Setup required parameters.

        :param str admin_username: admin authentication username
        :param str admin_password: admin authentication password
        :param str admin_isp_name: admin isp name
        :param str name: admin real name
        :param str email: admin email
        :param str comment: comment about this action
        :param bool admin_has_otp: has admin otp
        :param int admin_request_limit: limitation on admin requests

        :return: None
        :rtype: None
        """
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.admin_isp_name = admin_isp_name
        self.name = name
        self.email = email
        self.comment = comment
        self.admin_has_otp = admin_has_otp
        self.admin_request_limit = admin_request_limit
