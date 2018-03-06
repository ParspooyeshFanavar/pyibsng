""" info API method."""
from ibsng.handler.handler import Handler


class addGateway(Handler):
    """ info method class."""

    def setup(self, gateway_name, gateway_type, owner_isp_name, priority, comment, attributes):
        """Setup required parameters.

        :param str gateway_name: 
        :param choice gateway_type: 
        :param str owner_isp_name: 
        :param int priority: 
        :param str comment: 
        :param dict attributes: 
    
        :return: void
        :rtype: void
        """
        self.gateway_name = gateway_name
        self.gateway_type = gateway_type
        self.owner_isp_name = owner_isp_name
        self.priority = priority
        self.comment = comment
        self.attributes = attributes
