""" info API method."""
from ibsng.handler.handler import Handler


class updateGroup(Handler):
    """ info method class."""

    def setup(self, group_id, group_name, comment):
        """Setup required parameters.

        :param int group_id: 
        :param str group_name: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.group_id = group_id
        self.group_name = group_name
        self.comment = comment
