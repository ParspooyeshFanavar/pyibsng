"""Get user info API method."""
from ibsng.handler.handler import Handler


class getUserInfo(Handler):
    """Get user info class."""

    def setup(self, user_id=None, normal_username=None,
              voip_username=None, serial=None, phone=None):
        """Setup required parameters.

        :param str user_id: IBSng user id
        :param str normal_username: authentication username
        :param str voip_username: voip username
        :param str serial: serial code
        :param str phone: phone number

        :return: None
        :rtype: None
        """
        if user_id:
            self.user_id = user_id
        elif normal_username:
            self.normal_username = normal_username
        elif voip_username:
            self.voip_username = voip_username
        elif serial:
            self.serial = serial
        elif phone:
            self.phone = phone
