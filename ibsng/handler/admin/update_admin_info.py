"""Update admin info API method."""
from ibsng.handler.handler import Handler


class updateAdminInfo(Handler):
    """Update admin info class."""

    def setup(self, admin_id, admin_username, admin_isp_name, admin_locked,
              name, email, comment, admin_has_otp, admin_request_limit):
        """Setup required parameters.

        :param int admin_id: admin id
        :param str admin_username: admin authentication username
        :param str admin_isp_name: admin isp name
        :param bool admin_locked: lock admin
        :param name name: admin real name
        :param name email: admin email address
        :param name comment: comment about this action
        :param bool admin_has_otp: has admin otp
        :param int admin_request_limit: limitation on admin requests

        :return: None
        :rtype: None
        """
        self.admin_id = admin_id
        self.admin_username = admin_username
        self.admin_isp_name = admin_isp_name
        self.admin_locked = admin_locked
        self.name = name
        self.email = email
        self.comment = comment
        self.admin_has_otp = admin_has_otp
