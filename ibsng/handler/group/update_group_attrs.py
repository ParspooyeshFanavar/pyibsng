"""Update group attributes API method."""
from ibsng.handler.handler import Handler


class updateGroupAttrs(Handler):
    """Update group attributes method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.group_name, int)
        self.is_valid(self.attrs, dict, False)
        self.is_valid(self.to_del_attrs, list, False)

    def setup(self, group_name, attrs, to_del_attrs):
        """Setup required parameters.

        :param str group_name: group name
        :param dict attrs: updated attributes
        :param list to_del_attrs: deleted attributes

        :return: None
        :rtype: None
        """
        self.group_name = group_name
        self.attrs = attrs
        self.to_del_attrs = to_del_attrs
