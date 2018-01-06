"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class updateBwStaticIP(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, static_ip_id, ip_addr, tx_leaf_name, rx_leaf_name):
        """Setup required parameters.

        :param int static_ip_id: 
        :param str ip_addr: 
        :param str tx_leaf_name: 
        :param str rx_leaf_name: 
    
        :return: void
        :rtype: void
        """
        self.static_ip_id = static_ip_id
        self.ip_addr = ip_addr
        self.tx_leaf_name = tx_leaf_name
        self.rx_leaf_name = rx_leaf_name
