""" info API method."""
from ibsng.handler.handler import Handler


class addNewLoadBalancingIPpool(Handler):
    """ info method class."""

    def setup(self, ippool_name, ippool_comment, balancing_strategy, children_ippool_percentages):
        """Setup required parameters.

        :param str ippool_name: 
        :param str ippool_comment: 
        :param choice balancing_strategy: 
        :param dict children_ippool_percentages: keys are IPPool Names, values are percentage numbers
    
        :return: void
        :rtype: void
        """
        self.ippool_name = ippool_name
        self.ippool_comment = ippool_comment
        self.balancing_strategy = balancing_strategy
        self.children_ippool_percentages = children_ippool_percentages
