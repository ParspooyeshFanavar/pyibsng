"""Update leaf service API method."""
from ibsng.handler.handler import Handler


class updateLeafService(Handler):
    """Update leaf service class."""

    def setup(self, leaf_name, leaf_service_id, dst_ip, protocol,
              filter_, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str leaf_name: leaf name
        :param int leaf_service_id: leaf service ID
        :param str dst_ip: new destination IP
        :param str protocol: new protocol (choice: tcp, udp, icmp, ip)
        :param str filter: format: 'sport COMMA_SEPARATED_PORTS' or 
                           'dport COMMA_SEPARATED_PORTS' 
        :param int rate_kbits: new kilo bits
        :param int ceil_kbits: new kilo bits
        :param int priority: new priority
    
        :return: void
        :rtype: void
        """
        self.leaf_name = leaf_name
        self.leaf_service_id = leaf_service_id
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.filter_ = filter_
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
