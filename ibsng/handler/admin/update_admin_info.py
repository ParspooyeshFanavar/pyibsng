"""Update admin info API method."""
from ibsng.handler.handler import Handler


class updateAdminInfo(Handler):
    """Update admin info class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.admin_id, int)
        self.is_valid(self.admin_username, str)
        self.is_valid(self.admin_isp_name, str)
        self.is_valid(self.admin_locked, bool)
        self.is_valid(self.name, str)
        self.is_valid(self.email, str)
        self.is_valid_content(self.email, self.EMAIL_PATTERN)
        self.is_valid(self.comment, str, False)
        self.is_valid(self.admin_has_otp, bool)
        self.is_valid(self.admin_request_limit, int)

    def setup(self, admin_id, admin_username, admin_isp_name, admin_locked,
              name, email, admin_has_otp, admin_request_limit, comment=""):
        """Setup required parameters.

        :param int admin_id: admin id
        :param str admin_username: admin authentication username
        :param str admin_isp_name: admin isp name
        :param bool admin_locked: lock admin
        :param name name: admin real name
        :param name email: admin email address
        :param bool admin_has_otp: has admin otp
        :param int admin_request_limit: limitation on admin requests
        :param name comment: comment about this action

        :return: None
        :rtype: None
        """
        self.admin_id = admin_id
        self.admin_username = admin_username
        self.admin_isp_name = admin_isp_name
        self.admin_locked = admin_locked
        self.name = name
        self.email = email
        self.admin_has_otp = admin_has_otp
        self.admin_request_limit = admin_request_limit
        self.comment = comment
