"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class addLeafService(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, leaf_name, dst_ip, protocol, filter, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str leaf_name: 
        :param str dst_ip: 
        :param choice protocol: 
        :param str filter: format: 'sport COMMA_SEPARATED_PORTS' or 'dport COMMA_SEPARATED_PORTS'
        :param int rate_kbits: kilo bit
        :param int ceil_kbits: kilo bit
        :param int priority: 
    
        :return: void
        :rtype: void
        """
        self.leaf_name = leaf_name
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.filter = filter
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
