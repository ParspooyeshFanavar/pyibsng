"""Update bandwidth static IP API method."""
from ibsng.handler.handler import Handler


class updateBwStaticIP(Handler):
    """Update bandwidth static IP class."""

    def setup(self, static_ip_id, ip_addr, tx_leaf_name, rx_leaf_name):
        """Setup required parameters.

        :param int static_ip_id: static IP ID
        :param str ip_addr: new IP address
        :param str tx_leaf_name: new leaf name
        :param str rx_leaf_name: new leaf name

        :return: None
        :rtype: None
        """
        self.static_ip_id = static_ip_id
        self.ip_addr = ip_addr
        self.tx_leaf_name = tx_leaf_name
        self.rx_leaf_name = rx_leaf_name
