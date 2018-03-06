"""Update node API method."""
from ibsng.handler.handler import Handler


class updateNode(Handler):
    """Update node class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.node_id, int)
        self.is_valid_content(self.node_id, self.ID_PATTERN)
        self.is_valid(self.rate_kbits, int)
        self.is_valid(self.ceil_kbits, int)
        self.is_valid(self.priority, int)
        self.is_valid_content(self.priority, self.POSITIVE_NUMBER)

    def setup(self, node_id, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param int node_id: node ID
        :param int rate_kbits: new kilo bits
        :param int ceil_kbits: new kilo bits
        :param int priority: new priority

        :return: None
        :rtype: None
        """
        self.node_id = node_id
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
