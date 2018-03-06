"""Get node info API method."""
from ibsng.handler.handler import Handler


class getNodeInfo(Handler):
    """Get node info class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.node_id, int)
        self.is_valid_content(self.node_id, self.ID_PATTERN)

    def setup(self, node_id):
        """Setup required parameters.

        :param int node_id: node id

        :return: None
        :rtype: None
        """
        self.node_id = node_id
