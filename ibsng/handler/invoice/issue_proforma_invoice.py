"""Issue performa invoice API method."""
from ibsng.handler.handler import Handler


class issueProformaInvoice(Handler):
    """Issue performa invoice method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.attrs_list, list)
        self.is_valid(self.arbitrary_amount, float)

    def setup(self, attrs_list, arbitrary_amount):
        """Setup required parameters.

        :param list attrs_list: list of attributes
        :param float arbitrary_amount: arbitrary amount

        :return: None
        :rtype: None
        """
        self.arbitrary_amount = arbitrary_amount
        self.attrs_list = attrs_list
