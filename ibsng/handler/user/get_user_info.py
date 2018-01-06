""" info API method."""
from ibsng.handler.handler import Handler


class getUserInfo(Handler):
    """ info method class."""

    def setup(self, user_id=None, normal_username=None, voip_username=None, serial=None, phone=None):
        """Setup required parameters.

        :param str_int user_id: 
        :param str normal_username: 
        :param str voip_username: 
        :param str serial: 
        :param str phone: 
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.normal_username = normal_username
        self.voip_username = voip_username
        self.serial = serial
        self.phone = phone
