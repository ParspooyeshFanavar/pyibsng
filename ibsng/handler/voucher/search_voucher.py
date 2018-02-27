"""Search voucher API method."""
from ibsng.handler.handler import Handler


class searchVoucher(Handler):
    """Search voucher method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.from_index, int)
        self.is_valid(self.to_index, int)
        self.is_valid(self.sort_by, str)
        self.is_valid(self.desc, bool)

    def setup(self, conds, from_index, to_index, sort_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int from_index: from index for pagination
        :param int to_index: end index for pagination
        :param str sort_by: sort result by specific field ()
        :param bool desc: descending

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.from_index = from_index
        self.to_index = to_index
        self.sort_by = sort_by
        self.desc = desc
