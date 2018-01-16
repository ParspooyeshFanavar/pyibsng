"""Update leaf API method."""
from ibsng.handler.handler import Handler


class updateLeaf(Handler):
    """Update leaf class."""

    def setup(self, leaf_id, leaf_name, default_rate_kbits, default_ceil_kbits,
              total_rate_kbits, total_ceil_kbits, default_priority, total_priority):
        """Setup required parameters.

        :param int leaf_id: leaf ID
        :param str leaf_name: new leaf name
        :param int default_rate_kbits: new kilo bits
        :param int default_ceil_kbits: new kilo bits
        :param int total_rate_kbits: new kilo bits
        :param int total_ceil_kbits: new kilo bits
        :param int default_priority: new default priority
        :param int total_priority: new total priority

        :return: None
        :rtype: None
        """
        self.leaf_id = leaf_id
        self.leaf_name = leaf_name
        self.default_rate_kbits = default_rate_kbits
        self.default_ceil_kbits = default_ceil_kbits
        self.total_rate_kbits = total_rate_kbits
        self.total_ceil_kbits = total_ceil_kbits
        self.default_priority = default_priority
        self.total_priority = total_priority
