"""Get user info API method."""
from ibsng.handler.handler import Handler


class getUserInfo(Handler):
    """Get user info class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        if hasattr(self, "user_id"):
            self.is_valid(self.user_id, int)
        if hasattr(self, "normal_username"):
            self.is_valid(self.normal_username, str)
        if hasattr(self, "voip_username"):
            self.is_valid(self.voip_username, str)
        if hasattr(self, "serial"):
            self.is_valid(self.serial, str)
        if hasattr(self, "phone"):
            self.is_valid(self.phone, str)

    def setup(self, user_id=None, normal_username=None,
              voip_username=None, serial=None, phone=None):
        """Setup required parameters.

        :param int user_id: ibsng user id
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
