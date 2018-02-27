"""Search admin login history API method."""
from ibsng.handler.handler import Handler


class searchAdminLoginHistory(Handler):
    """Search admin login history method class."""

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
        :param int from_index: from index
        :param int to_index: end index
        :param str sort_by: sort result by specific field
        :param bool desc: descending

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.__from = from_index
        self.to_ = to_index
        self.sort_by = sort_by
        self.desc = desc
