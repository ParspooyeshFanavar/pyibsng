"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class getRealHostInterfaces(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, hostname, host_type):
        """Setup required parameters.

        :param str hostname: 
        :param choice host_type: 
    
        :return: void
        :rtype: void
        """
        self.hostname = hostname
        self.host_type = host_type
