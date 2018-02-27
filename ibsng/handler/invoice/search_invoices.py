"""Search invoice API method."""
from ibsng.handler.handler import Handler


class searchInvoices(Handler):
    """Search invoice method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.__from, int)
        self.is_valid(self.to_, int)
        self.is_valid(self.sort_by, str)
        self.is_valid(self.desc, bool)

    def setup(self, conds, _from, to_, sort_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int _from: pagination start
        :param int to: pagination end
        :param choice sort_by: sort result by specific field
        :param bool desc: descending order

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.__from = _from
        self.to_ = to_
        self.sort_by = sort_by
        self.desc = desc
