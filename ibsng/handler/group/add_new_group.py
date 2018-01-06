""" info API method."""
from ibsng.handler.handler import Handler


class addNewGroup(Handler):
    """ info method class."""

    def setup(self, group_name, comment, isp_name):
        """Setup required parameters.

        :param str group_name: 
        :param str comment: 
        :param str isp_name: 
    
        :return: void
        :rtype: void
        """
        self.group_name = group_name
        self.comment = comment
        self.isp_name = isp_name
