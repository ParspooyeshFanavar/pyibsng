"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class addLeaf(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, leaf_name, parent_id, default_rate_kbits, default_ceil_kbits, total_rate_kbits, total_ceil_kbits, default_priority, total_priority):
        """Setup required parameters.

        :param str leaf_name: 
        :param int parent_id: 
        :param int default_rate_kbits: kilo bits
        :param int default_ceil_kbits: kilo bits
        :param int total_rate_kbits: kilo bits
        :param int total_ceil_kbits: kilo bits
        :param int default_priority: 
        :param int total_priority: 
    
        :return: void
        :rtype: void
        """
        self.leaf_name = leaf_name
        self.parent_id = parent_id
        self.default_rate_kbits = default_rate_kbits
        self.default_ceil_kbits = default_ceil_kbits
        self.total_rate_kbits = total_rate_kbits
        self.total_ceil_kbits = total_ceil_kbits
        self.default_priority = default_priority
        self.total_priority = total_priority
