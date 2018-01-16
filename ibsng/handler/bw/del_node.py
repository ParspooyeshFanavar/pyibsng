"""Delete node API method."""
from ibsng.handler.handler import Handler


class delNode(Handler):
    """Delete node class."""

    def setup(self, node_id):
        """Setup required parameters.

        :param int node_id: node ID

        :return: None
        :rtype: None
        """
        self.node_id = node_id
