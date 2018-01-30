"""Update group API method."""
from ibsng.handler.handler import Handler


class updateGroup(Handler):
    """Update group method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_id, int)
        self.is_valid(self.group_name, str)
        self.is_valid(self.status, str)
        self.is_valid(self.comment, str, False)

    def setup(self, group_id, group_name, status, comment=""):
        """Setup required parameters.

        :param int group_id: group id
        :param str group_name: new group name
        :param str status: status of group
        :param str comment: new group comment

        :return: None
        :rtype: None
        """
        self.group_id = group_id
        self.group_name = group_name
        self.status = status
        self.comment = comment
