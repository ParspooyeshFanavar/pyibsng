""" info API method."""
from ibsng.handler.handler import Handler


class copyGroup(Handler):
    """ info method class."""

    def setup(self, group_name, comment, isp_name, copy_count):
        """Setup required parameters.

        :param str group_name: 
        :param str comment: 
        :param str isp_name: 
        :param int copy_count: 
    
        :return: void
        :rtype: void
        """
        self.group_name = group_name
        self.comment = comment
        self.isp_name = isp_name
        self.copy_count = copy_count
