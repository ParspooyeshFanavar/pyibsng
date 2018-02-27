"""Voucher search batch API method."""
from ibsng.handler.handler import Handler


class voucherSearchBatch(Handler):
    """Voucher search batch method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.index_from, int)
        self.is_valid(self.index_to, int)
        self.is_valid(self.sort_by, str)
        self.is_valid(self.desc, str)

    def setup(self, conds, index_from, index_to, sort_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int index_from: start index for pagination
        :param int index_to: end index for pagination
        :param str sort_by: sort by specific field (batch_id,
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
