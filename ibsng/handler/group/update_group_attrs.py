""" info API method."""
from ibsng.handler.handler import Handler


class updateGroupAttrs(Handler):
    """ info method class."""

    def setup(self, group_name, attrs, to_del_attrs):
        """Setup required parameters.

        :param str group_name: 
        :param dict attrs: 
        :param list to_del_attrs: 
    
        :return: void
        :rtype: void
        """
        self.group_name = group_name
        self.attrs = attrs
        self.to_del_attrs = to_del_attrs
