"""Add new group API method."""
from ibsng.handler.handler import Handler


class addNewGroup(Handler):
    """Add new group method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_name, str)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.status, str)
        self.is_valid(self.comment, str, False)

    def setup(self, group_name, isp_name, status, comment=""):
        """Setup required parameters.

        :param str group_name: group name
        :param str isp_name: isp name
        :param str status: status of group
        :param str comment: group comment

        :return: None
        :rtype: None
        """
        self.group_name = group_name
        self.isp_name = isp_name
        self.status = status
        self.comment = comment
