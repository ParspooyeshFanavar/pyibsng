"""Update leaf service API method."""
from ibsng.handler.handler import Handler


class updateLeafService(Handler):
    """Update leaf service class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.leaf_name, str)
        self.is_valid(self.leaf_service_id, int)
        self.is_valid_content(self.leaf_service_id, self.ID_PATTERN)
        self.is_valid(self.dst_ip, str)
        self.is_valid_content(self.dst_ip, self.IP_PATTERN)
        self.is_valid(self.leaf_name, str)
        self.is_valid(self.protocol, str)
        self.is_valid_content(self.protocol, "(tcp|udp|icmp|ip)")
        self.is_valid(self.filter_, str)
        self.is_valid(self.rate_kbits, int)
        self.is_valid(self.ceil_kbits, int)
        self.is_valid(self.priority, int)
        self.is_valid_content(self.priority, self.POSITIVE_NUMBER)

    def setup(self, leaf_name, leaf_service_id, dst_ip, protocol,
              filter_format, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str leaf_name: leaf name
        :param int leaf_service_id: leaf service ID
        :param str dst_ip: new destination IP
        :param str protocol: new protocol (choice: tcp, udp, icmp, ip)
        :param str filter_format: format: 'sport COMMA_SEPARATED_PORTS' or
                                  'dport COMMA_SEPARATED_PORTS'
        :param int rate_kbits: new kilo bits
        :param int ceil_kbits: new kilo bits
        :param int priority: new priority

        :return: None
        :rtype: None
        """
        self.leaf_name = leaf_name
        self.leaf_service_id = leaf_service_id
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.filter_ = filter_format
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
