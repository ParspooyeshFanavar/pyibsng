"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class getNodeInfo(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, node_id):
        """Setup required parameters.

        :param int node_id: 
    
        :return: void
        :rtype: void
        """
        self.node_id = node_id
