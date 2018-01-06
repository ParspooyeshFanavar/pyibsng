"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class delLeafService(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, leaf_service_id, leaf_name):
        """Setup required parameters.

        :param int leaf_service_id: 
        :param str leaf_name: 
    
        :return: void
        :rtype: void
        """
        self.leaf_service_id = leaf_service_id
        self.leaf_name = leaf_name
