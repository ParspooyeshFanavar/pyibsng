"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class addNode(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, hostname, interface_name, parent_id, rate_kbits, ceil_kbits, priority):
        """Setup required parameters.

        :param str hostname: 
        :param str interface_name: 
        :param int parent_id: 
        :param int rate_kbits: kilo bits
        :param int ceil_kbits: kilo bits
        :param int priority: 
    
        :return: void
        :rtype: void
        """
        self.hostname = hostname
        self.interface_name = interface_name
        self.parent_id = parent_id
        self.rate_kbits = rate_kbits
        self.ceil_kbits = ceil_kbits
        self.priority = priority
