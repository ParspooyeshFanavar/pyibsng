"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class getLeafInfo(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, leaf_name):
        """Setup required parameters.

        :param str leaf_name: 
    
        :return: void
        :rtype: void
        """
        self.leaf_name = leaf_name
