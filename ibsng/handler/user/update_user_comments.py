""" info API method."""
from ibsng.handler.handler import Handler


class updateUserComments(Handler):
    """ info method class."""

    def setup(self, update_dic):
        """Setup required parameters.

        :param dict update_dic: 
    
        :return: void
        :rtype: void
        """
        self.update_dic = update_dic
