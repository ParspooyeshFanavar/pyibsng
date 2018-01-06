""" info API method."""
from ibsng.handler.handler import Handler


class addNewUsers(Handler):
    """ info method class."""

    def setup(self, count, credit, isp_name, group_name, credit_comment, custom_fields=None):
        """Setup required parameters.

        :param int count: 
        :param float credit: 
        :param str isp_name: 
        :param str group_name: 
        :param str credit_comment: 
        :param dict custom_fields: 
    
        :return: void
        :rtype: void
        """
        self.count = count
        self.credit = credit
        self.isp_name = isp_name
        self.group_name = group_name
        self.credit_comment = credit_comment
        self.custom_fields = custom_fields
