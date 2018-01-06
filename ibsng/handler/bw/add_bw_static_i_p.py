"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class addBwStaticIP(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, ip_addr, tx_leaf_name, rx_leaf_name):
        """Setup required parameters.

        :param str ip_addr: 
        :param str tx_leaf_name: 
        :param str rx_leaf_name: 
    
        :return: void
        :rtype: void
        """
        self.ip_addr = ip_addr
        self.tx_leaf_name = tx_leaf_name
        self.rx_leaf_name = rx_leaf_name
