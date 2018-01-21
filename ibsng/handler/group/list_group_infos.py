""" info API method."""
from ibsng.handler.handler import Handler


class listGroupInfos(Handler):
    """ info method class."""

    def setup(self, isp_id, active_only=None):
        """Setup required parameters.

        :param bool active_only: pass true if you only want active groups
        :param str isp_id: comma-seprated. list of isp ids
    
        :return: void
        :rtype: void
        """
        self.active_only = active_only
        self.isp_id = isp_id
