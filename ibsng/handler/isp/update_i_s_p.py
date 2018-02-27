"""Update ISP API method."""
from ibsng.handler.handler import Handler


class updateISP(Handler):
    """Update ISP method class."""

    def control(self):
        """Validate inputs after method setup

        :return: None
        :rtype: None
        """

        self.is_valid(self.isp_id, int)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.parent_isp_name, str)
        self.is_valid(self.isp_has_deposit_limit, bool)
        self.is_valid(self.isp_mapped_user_id, int)
        self.is_valid(self.isp_auth_domain, str)
        self.is_valid(self.isp_web_domain, str)
        self.is_valid(self.isp_email, str)
        self.is_valid(self.prevent_neg_deposit_login, bool)
        self.is_valid(self.isp_comment, str)
        self.is_valid(self.isp_failed_user_id, int)
        self.is_valid(self.isp_locked, bool)

    def setup(self, isp_id, isp_name, parent_isp_name, isp_has_deposit_limit, isp_mapped_user_id, isp_auth_domain,
              isp_web_domain, isp_email, prevent_neg_deposit_login, isp_comment, isp_failed_user_id, isp_locked):
        """Setup required parameters.

        :param int isp_id: isp id
        :param str isp_name: isp name
        :param str parent_isp_name: parent isp name
        :param bool isp_has_deposit_limit: isp has deposit limit
        :param int isp_mapped_user_id: isp mapped user id
        :param str isp_auth_domain: isp auth domain
        :param str isp_web_domain: isp web domain
        :param str isp_email: isp email
        :param bool prevent_neg_deposit_login: prevent neg deposit login
        :param str isp_comment: isp comment
        :param int isp_failed_user_id: isp failed user id
        :param bool isp_locked: isp locked
        :return: None
        :rtype: None
        """

        self.isp_id = isp_id
        self.isp_name = isp_name
        self.parent_isp_name = parent_isp_name
        self.isp_has_deposit_limit = isp_has_deposit_limit
        self.isp_mapped_user_id = isp_mapped_user_id
        self.isp_auth_domain = isp_auth_domain
        self.isp_web_domain = isp_web_domain
        self.isp_email = isp_email
        self.prevent_neg_deposit_login = prevent_neg_deposit_login
        self.isp_comment = isp_comment
        self.isp_failed_user_id = isp_failed_user_id
        self.isp_locked = isp_locked
