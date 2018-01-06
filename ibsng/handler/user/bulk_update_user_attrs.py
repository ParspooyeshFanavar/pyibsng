""" info API method."""
from ibsng.handler.handler import Handler


class bulkUpdateUserAttrs(Handler):
    """ info method class."""

    def setup(self, conds, attrs_to_update, attrs_to_del):
        """Setup required parameters.

        :param dict conds: the same as method 'user.searchUser', parameter 'conds'
        :param dict attrs_to_update: the same as method 'user.updateUserAttrs', parameter 'attrs'
        :param list attrs_to_del: the same as method 'user.updateUserAttrs', parameter 'to_del_attrs'
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.attrs_to_update = attrs_to_update
        self.attrs_to_del = attrs_to_del
