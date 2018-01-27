"""Bulk action to update user attrs API method."""
from ibsng.handler.handler import Handler


class bulkUpdateUserAttrs(Handler):
    """Bulk action to update user attrs method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.attrs_to_update, dict, False)
        self.is_valid(self.attrs_to_del, list, False)

    def setup(self, conds, attrs_to_update={}, attrs_to_del=[]):
        """Setup required parameters.

        :param dict conds: conditions
        :param dict attrs_to_update: attributes with new values
        :param list attrs_to_del: list of attributes which should be deleted

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.attrs_to_update = attrs_to_update
        self.attrs_to_del = attrs_to_del
