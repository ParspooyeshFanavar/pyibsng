"""Update bandwidth static IP API method."""
from ibsng.handler.handler import Handler


class updateBwStaticIP(Handler):
    """Update bandwidth static IP class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.static_ip_id, int)
        self.is_valid_content(self.static_ip_id, self.ID_PATTERN)
        self.is_valid(self.ip_addr, str)
        self.is_valid_content(self.ip_addr, self.IP_PATTERN)
        self.is_valid(self.tx_leaf_name, str)
        self.is_valid(self.rx_leaf_name, str)

    def setup(self, static_ip_id, ip_addr, tx_leaf_name, rx_leaf_name):
        """Setup required parameters.

        :param int static_ip_id: static ip id
        :param str ip_addr: new ip address
        :param str tx_leaf_name: new leaf name
        :param str rx_leaf_name: new leaf name

        :return: None
        :rtype: None
        """
        self.static_ip_id = static_ip_id
        self.ip_addr = ip_addr
        self.tx_leaf_name = tx_leaf_name
        self.rx_leaf_name = rx_leaf_name
