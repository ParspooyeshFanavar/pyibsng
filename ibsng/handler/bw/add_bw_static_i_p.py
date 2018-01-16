"""Add bandwidth static IP API method."""
from ibsng.handler.handler import Handler


class addBwStaticIP(Handler):
    """Add bandwidth static IP class."""

    def setup(self, ip_addr, tx_leaf_name, rx_leaf_name):
        """Setup required parameters.

        :param str ip_addr: IP address
        :param str tx_leaf_name: leaf name
        :param str rx_leaf_name: leaf name 

        :return: None
        :rtype: None
        """
        self.ip_addr = ip_addr
        self.tx_leaf_name = tx_leaf_name
        self.rx_leaf_name = rx_leaf_name
