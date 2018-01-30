"""Delete group API method."""
from ibsng.handler.handler import Handler


class delGroup(Handler):
    """Delete group method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_name, str)

    def setup(self, group_name):
        """Setup required parameters.

        :param str group_name: group name

        :return: None
        :rtype: None
        """
        self.group_name = group_name
