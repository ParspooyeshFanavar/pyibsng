"""Search batch API method."""
from ibsng.handler.handler import Handler


class searchBatch(Handler):
    """Search batch method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.index_from, int)
        self.is_valid(self.index_to, int)
        self.is_valid(self.sort_by, str)
        self.is_valid(self.desc, bool)

    def setup(self, conds, index_from, index_to, sort_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int index_from: from index
        :param int index_to: end index
        :param str sort_by: sort result by specific field (batch_id,
                            batch_name, batch_credit)
        :param bool desc: descending

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.index_from = index_from
        self.index_to = index_to
        self.sort_by = sort_by
        self.desc = desc
