"""Add new load balancing ip pool API method."""
from ibsng.handler.handler import Handler


class addNewLoadBalancingIPpool(Handler):
    """Add new load balancing ip pool method class."""

    def control(self):
        """Validate inputs after method setup.

        :return: None
        :rtype: None
        """
        self.is_valid(self.ippool_name, str)
        self.is_valid(self.ippool_comment, str)
        self.is_valid_choice(self.balancing_strategy,
                             ['distributive', 'fill_first'])
        self.is_valid(self.children_ippool_percentages, dict)

    def setup(self, ippool_name, ippool_comment,
              balancing_strategy, children_ippool_percentages):
        """Setup required parameters.

        :param str ippool_name: ip pool name
        :param str ippool_comment: ip pool comment
        :param choice balancing_strategy: balancing strategy
        :param dict children_ippool_percentages: keys are IPPool Names, values
                                                 are percentage numbers

        :return: None
        :rtype: None
        """
        self.ippool_name = ippool_name
        self.ippool_comment = ippool_comment
        self.balancing_strategy = balancing_strategy
        self.children_ippool_percentages = children_ippool_percentages
