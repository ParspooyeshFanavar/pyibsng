""" info API method."""
from ibsng.handler.handler import Handler


class addNewAdmin(Handler):
    """ info method class."""

    def setup(self, admin_username, admin_password, admin_isp_name, name, email, comment, admin_has_otp, admin_request_limit):
        """Setup required parameters.

        :param str admin_username: 
        :param str admin_password: 
        :param str admin_isp_name: 
        :param str name: 
        :param str email: 
        :param str comment: 
        :param bool admin_has_otp: 
        :param int admin_request_limit: 
    
        :return: void
        :rtype: void
        """
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.admin_isp_name = admin_isp_name
        self.name = name
        self.email = email
        self.comment = comment
        self.admin_has_otp = admin_has_otp
        self.admin_request_limit = admin_request_limit
