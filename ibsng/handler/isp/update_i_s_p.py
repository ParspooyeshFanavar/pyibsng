""" info API method."""
from ibsng.handler.handler import Handler


class updateISP(Handler):
    """ info method class."""

    def setup(self, isp_id, isp_name, parent_isp_name, isp_has_deposit_limit, isp_mapped_user_id, isp_auth_domain, isp_web_domain, isp_email, prevent_neg_deposit_login, isp_comment, isp_failed_user_id, isp_locked):
        """Setup required parameters.

        :param int isp_id: 
        :param str isp_name: 
        :param str parent_isp_name: 
        :param bool isp_has_deposit_limit: 
        :param int isp_mapped_user_id: 
        :param str isp_auth_domain: 
        :param str isp_web_domain: 
        :param str isp_email: 
        :param bool prevent_neg_deposit_login: 
        :param str isp_comment: 
        :param int isp_failed_user_id: removed in C_dev_326
        :param bool isp_locked: 
    
        :return: void
        :rtype: void
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
