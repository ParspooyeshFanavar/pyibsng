""" info API method."""
from ibsng.handler.handler import Handler


class updateUserAttrs(Handler):
    """ info method class."""

    def setup(self, user_id, attrs, to_del_attrs):
        """Setup required parameters.

        :param str user_id: 
        :param dict attrs: 
        :param list to_del_attrs: list of attributes to be deleted
    
        :return: void
        :rtype: void
        """
        self.user_id = user_id
        self.attrs = attrs
        self.to_del_attrs = to_del_attrs
