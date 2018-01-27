"""Delete leaf service API method."""
from ibsng.handler.handler import Handler


class delLeafService(Handler):
    """Delete leaf service class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.leaf_service_id, self.ID_PATTERN)
        self.is_valid(self.leaf_name, str)

    def setup(self, leaf_service_id, leaf_name):
        """Setup required parameters.

        :param int leaf_service_id: leaf service ID
        :param str leaf_name: leaf name

        :return: None
        :rtype: None
        """
        self.leaf_service_id = leaf_service_id
        self.leaf_name = leaf_name
