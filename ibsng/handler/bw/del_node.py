"""Delete node API method."""
from ibsng.handler.handler import Handler


class delNode(Handler):
    """Delete node class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.node_id, int)
        self.is_valid_content(self.node_id, self.IP_PATTERN)

    def setup(self, node_id):
        """Setup required parameters.

        :param int node_id: node ID

        :return: None
        :rtype: None
        """
        self.node_id = node_id
