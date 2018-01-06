"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class getBwStaticIPInfo(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, ip_addr):
        """Setup required parameters.

        :param str ip_addr: 
    
        :return: void
        :rtype: void
        """
        self.ip_addr = ip_addr
