""" info API method."""
from ibsng.handler.handler import Handler


class updateAdminInfo(Handler):
    """ info method class."""

    def setup(self, admin_id, admin_username, admin_isp_name, admin_locked, name, email, comment, admin_has_otp):
        """Setup required parameters.

        :param int admin_id: 
        :param str admin_username: 
        :param str admin_isp_name: 
        :param bool admin_locked: 
        :param name name: 
        :param name email: 
        :param name comment: 
        :param bool admin_has_otp: 
    
        :return: void
        :rtype: void
        """
        self.admin_id = admin_id
        self.admin_username = admin_username
        self.admin_isp_name = admin_isp_name
        self.admin_locked = admin_locked
        self.name = name
        self.email = email
        self.comment = comment
        self.admin_has_otp = admin_has_otp
