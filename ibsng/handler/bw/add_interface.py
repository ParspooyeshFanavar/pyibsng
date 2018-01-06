"""bandwidth limit, based on tag C_lan_acc_staging_327 info API method."""
from ibsng.handler.handler import Handler


class addInterface(Handler):
    """bandwidth limit, based on tag C_lan_acc_staging_327 info method class."""

    def setup(self, hostname, interface_name, comment, host_type):
        """Setup required parameters.

        :param str hostname: 
        :param str interface_name: 
        :param str comment: 
        :param choice host_type: 
    
        :return: void
        :rtype: void
        """
        self.hostname = hostname
        self.interface_name = interface_name
        self.comment = comment
        self.host_type = host_type
