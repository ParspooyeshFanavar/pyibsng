"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class getTree(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, hostname, interface_name):
        """Setup required parameters.

        :param str hostname: 
        :param str interface_name: 
    
        :return: void
        :rtype: void
        """
        self.hostname = hostname
        self.interface_name = interface_name
