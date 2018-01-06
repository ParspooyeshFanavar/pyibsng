""" info API method."""
from ibsng.handler.handler import Handler


class getGroupInfo(Handler):
    """ info method class."""

    def setup(self, group_name=None, group_id=None):
        """Setup required parameters.

        :param str group_name: 
        :param str group_id: 
    
        :return: void
        :rtype: void
        """
        self.group_name = group_name
        self.group_id = group_id
