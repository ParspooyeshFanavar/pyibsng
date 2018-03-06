""" info API method."""
from ibsng.handler.handler import Handler


class getOnlineUsers(Handler):
    """ info method class."""

    def setup(self, normal_sort_by, normal_desc, voip_sort_by, voip_desc, conds):
        """Setup required parameters.

        :param choice normal_sort_by: 
        :param bool normal_desc: descending
        :param choice voip_sort_by: 
        :param bool voip_desc: descending
        :param dict conds: 
    
        :return: void
        :rtype: void
        """
        self.normal_sort_by = normal_sort_by
        self.normal_desc = normal_desc
        self.voip_sort_by = voip_sort_by
        self.voip_desc = voip_desc
        self.conds = conds
