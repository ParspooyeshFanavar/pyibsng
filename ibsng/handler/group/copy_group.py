"""Copy group API method."""
from ibsng.handler.handler import Handler


class copyGroup(Handler):
    """Copy group info method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_name, str)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.copy_count, int)
        self.is_valid(self.comment, str, False)

    def setup(self, group_name, isp_name, copy_count, comment=""):
        """Setup required parameters.

        :param str group_name: group name
        :param str isp_name: isp name
        :param int copy_count: count of copy
        :param str comment: group comment

        :return: None
        :rtype: None
        """
        self.group_name = group_name
        self.isp_name = isp_name
        self.copy_count = copy_count
        self.comment = comment
