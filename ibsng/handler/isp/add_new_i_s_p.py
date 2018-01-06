""" info API method."""
from ibsng.handler.handler import Handler


class addNewISP(Handler):
    """ info method class."""

    def setup(self, isp_name, parent_isp_name, isp_has_deposit_limit, isp_deposit, isp_mapped_user_id, isp_auth_domain, isp_web_domain, isp_email, prevent_neg_deposit_login, isp_comment, isp_failed_user_id):
        """Setup required parameters.

        :param str isp_name: 
        :param str parent_isp_name: 
        :param bool isp_has_deposit_limit: 
        :param float isp_deposit: float
        :param int isp_mapped_user_id: or -1
        :param str isp_auth_domain: or ''
        :param str isp_web_domain: or ''
        :param str isp_email: 
        :param bool prevent_neg_deposit_login: 
        :param str isp_comment: or ''
        :param int isp_failed_user_id: or -1, removed in C_dev_326
    
        :return: void
        :rtype: void
        """
        self.isp_name = isp_name
        self.parent_isp_name = parent_isp_name
        self.isp_has_deposit_limit = isp_has_deposit_limit
        self.isp_deposit = isp_deposit
        self.isp_mapped_user_id = isp_mapped_user_id
        self.isp_auth_domain = isp_auth_domain
        self.isp_web_domain = isp_web_domain
        self.isp_email = isp_email
        self.prevent_neg_deposit_login = prevent_neg_deposit_login
        self.isp_comment = isp_comment
        self.isp_failed_user_id = isp_failed_user_id
