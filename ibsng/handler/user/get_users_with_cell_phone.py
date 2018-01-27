"""Get users by cellphone API method."""
from ibsng.handler.handler import Handler


class getUsersWithCellPhone(Handler):
    """Get users by cellphone method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.cell_phone, str)

    def setup(self, cellphone):
        """Setup required parameters.

        :param str cellphone: ibsng users cellphone

        :return: None
        :rtype: None
        """
        self.cell_phone = cellphone
