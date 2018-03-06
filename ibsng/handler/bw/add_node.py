"""Add new node API method."""
from ibsng.handler.handler import Handler


class addNode(Handler):
    """Add new node class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.hostname, str)
        self.is_valid(self.interface_name, str)
        self.is_valid(self.parent_id, int)
        self.is_valid_content(self.parent_id, self.ID_PATTERN)
        self.is_valid(self.rate_kbits, int)
        self.is_valid(self.ceil_kbits, int)
        self.is_valid(self.priority, int)
        self.is_valid_content(self.priority, self.POSITIVE_NUMBER)

    def setup(self, hostname, interface_name, parent_id,
              rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str hostname: host name
        :param str interface_name: interface name
        :param int parent_id: parent node
        :param int rate_kbits: kilo bits
        :param int ceil_kbits: kilo bits
        :param int priority: node priority

        :return: None
        :rtype: None
        """
        self.hostname = hostname
        self.interface_name = interface_name
        self.parent_id = parent_id
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
