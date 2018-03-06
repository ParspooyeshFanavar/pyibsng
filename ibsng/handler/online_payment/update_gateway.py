""" info API method."""
from ibsng.handler.handler import Handler


class updateGateway(Handler):
    """ info method class."""

    def setup(self, gateway_id, gateway_name, owner_isp_name, priority, comment, attributes):
        """Setup required parameters.

        :param int gateway_id: 
        :param str gateway_name: 
        :param str owner_isp_name: 
        :param int priority: 
        :param str comment: 
        :param dict attributes: 
    
        :return: void
        :rtype: void
        """
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.owner_isp_name = owner_isp_name
        self.priority = priority
        self.comment = comment
        self.attributes = attributes
