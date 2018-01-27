"""Add new user API method."""
from ibsng.handler.handler import Handler


class addNewUsers(Handler):
    """Add new user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.count, int)
        self.is_valid(self.credit, float)
        self.is_valid(self.isp_name, str)
        self.is_valid(self.group_name, str)
        self.is_valid(self.credit_comment, str)
        self.is_valid(self.custom_fields, dict, False)

    def setup(self, count, credit, isp_name, group_name,
              credit_comment="", custom_fields={}):
        """Setup required parameters.

        :param int count: count of users
        :param float credit: initialize credit
        :param str isp_name: isp name
        :param str group_name: group name
        :param str credit_comment: credit comment
        :param dict custom_fields: custom fields

        :return: None
        :rtype: None
        """
        self.count = count
        self.credit = credit
        self.isp_name = isp_name
        self.group_name = group_name
        self.credit_comment = credit_comment
        self.custom_fields = custom_fields
