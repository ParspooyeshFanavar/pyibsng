"""Update user comments API method."""
from ibsng.handler.handler import Handler


class updateUserComments(Handler):
    """Update user comments method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.update_dic, dict)

    def setup(self, update_dict):
        """Setup required parameters.

        :param dict update_dict: key value attributes

        :return: None
        :rtype: None
        """
        self.update_dic = update_dict
