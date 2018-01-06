"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class updateNode(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, node_id, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param int node_id: 
        :param int rate_kbits: 
        :param int ceil_kbits: 
        :param int priority: 
    
        :return: void
        :rtype: void
        """
        self.node_id = node_id
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
