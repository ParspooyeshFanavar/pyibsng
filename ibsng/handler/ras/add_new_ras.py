""" info API method."""
from ibsng.handler.handler import Handler


class addNewRas(Handler):
    """ info method class."""

    def setup(self, ras_ip, ras_type, radius_secret, ras_description, comment):
        """Setup required parameters.

        :param str ras_ip: 
        :param choice ras_type: 
        :param str radius_secret: 
        :param str ras_description: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.ras_ip = ras_ip
        self.ras_type = ras_type
        self.radius_secret = radius_secret
        self.ras_description = ras_description
        self.comment = comment
