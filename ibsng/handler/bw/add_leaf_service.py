"""Add new leaf service API method."""
from ibsng.handler.handler import Handler


class addLeafService(Handler):
    """Add new leaf service class."""

    def setup(self, leaf_name, dst_ip, protocol, filter_, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str leaf_name: leaf name
        :param str dst_ip: destination IP address
        :param str protocol: protocol type (choice: tcp, udp, icmp, ip)
        :param str filter: format: 'sport COMMA_SEPARATED_PORTS' or 
                           'dport COMMA_SEPARATED_PORTS'
        :param int rate_kbits: kilo bit
        :param int ceil_kbits: kilo bit
        :param int priority: new service priority

        :return: None
        :rtype: None
        """
        self.leaf_name = leaf_name
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.filter_ = filter_
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
