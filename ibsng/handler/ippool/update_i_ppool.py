""" info API method."""
from ibsng.handler.handler import Handler


class updateIPpool(Handler):
    """ info method class."""

    def setup(self, ippool_id, ippool_name, comment):
        """Setup required parameters.

        :param int ippool_id: 
        :param str ippool_name: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.ippool_id = ippool_id
        self.ippool_name = ippool_name
        self.comment = comment
