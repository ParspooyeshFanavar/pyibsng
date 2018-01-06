"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class updateLeafService(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, leaf_name, leaf_service_id, dst_ip, protocol, filter, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str leaf_name: 
        :param int leaf_service_id: 
        :param str dst_ip: 
        :param choice protocol: 
        :param str filter: 
        :param int rate_kbits: 
        :param int ceil_kbits: 
        :param int priority: 
    
        :return: void
        :rtype: void
        """
        self.leaf_name = leaf_name
        self.leaf_service_id = leaf_service_id
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.filter = filter
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
