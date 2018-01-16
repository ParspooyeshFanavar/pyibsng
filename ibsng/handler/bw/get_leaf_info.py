"""Get leaf info API method."""
from ibsng.handler.handler import Handler


class getLeafInfo(Handler):
    """Get leaf info class."""

    def setup(self, leaf_name):
        """Setup required parameters.

        :param str leaf_name: leaf name

        :return: None
        :rtype: None
        """
        self.leaf_name = leaf_name
