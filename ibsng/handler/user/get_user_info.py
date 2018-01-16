""" info API method."""
from ibsng.handler.handler import Handler


class getUserInfo(Handler):
    """ info method class."""

    def setup(self, user_id=None, normal_username=None,
              voip_username=None, serial=None, phone=None):
        """Setup required parameters.

        :param str user_id: IBSng user id
        :param str normal_username: username
        :param str voip_username: voip username
        :param str serial: serial code
        :param str phone: phone number
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.normal_username = normal_username
        self.voip_username = voip_username
        self.serial = serial
        self.phone = phone

