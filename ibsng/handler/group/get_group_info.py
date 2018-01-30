"""Get group info API method."""
from ibsng.handler.handler import Handler


class getGroupInfo(Handler):
    """Get group info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_name, str, False)
        self.is_valid(self.group_id, int, False)

    def setup(self, group_name=None, group_id=None):
        """Setup required parameters.

        :param str group_name: group name
        :param str group_id: group id

        :return: None
        :rtype: None
        """
        if group_name:
            self.group_name = group_name
        elif group_id:
            self.group_id = group_id
