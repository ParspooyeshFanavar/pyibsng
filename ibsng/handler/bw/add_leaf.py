"""Add new leaf API method."""
from ibsng.handler.handler import Handler


class addLeaf(Handler):
    """Add new leaf class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.leaf_name, str)
        self.is_valid(self.parent_id, int)
        self.is_valid_content(self.parent_id, self.ID_PATTERN)
        self.is_valid(self.default_rate_kbits, int)
        self.is_valid(self.default_ceil_kbits, int)
        self.is_valid(self.total_rate_kbits, int)
        self.is_valid(self.total_ceil_kbits, int)
        self.is_valid(self.default_priority, int)
        self.is_valid(self.total_priority, int)

    def setup(self, leaf_name, parent_id, default_rate_kbits,
              default_ceil_kbits, total_rate_kbits, total_ceil_kbits,
              default_priority, total_priority):
        """Setup required parameters.

        :param str leaf_name: leaf name
        :param int parent_id: parent leaf
        :param int default_rate_kbits: kilo bits
        :param int default_ceil_kbits: kilo bits
        :param int total_rate_kbits: kilo bits
        :param int total_ceil_kbits: kilo bits
        :param int default_priority: default priority
        :param int total_priority: total priority

        :return: None
        :rtype: None
        """
        self.leaf_name = leaf_name
        self.parent_id = parent_id
        self.default_rate_kbits = default_rate_kbits
        self.default_ceil_kbits = default_ceil_kbits
        self.total_rate_kbits = total_rate_kbits
        self.total_ceil_kbits = total_ceil_kbits
        self.default_priority = default_priority
        self.total_priority = total_priority
