"""Update user attrs API method."""
from ibsng.handler.handler import Handler


class updateUserAttrs(Handler):
    """Update user attrs method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, int)
        self.is_valid(self.attrs, dict)
        self.is_valid(self.to_del_attrs, list)

    def setup(self, user_id, attrs, to_del_attrs):
        """Setup required parameters.

        :param str user_id: ibsng user id
        :param dict attrs: attributes with values
        :param list to_del_attrs: list of attributes to be deleted

        :return: None
        :rtype: None
        """
        self.user_id = user_id
        self.attrs = attrs
        self.to_del_attrs = to_del_attrs
