"""Search for OTPs API method."""
from ibsng.handler.handler import Handler


class searchOTPs(Handler):
    """Search for OTPs class."""

    def setup(self, conds, _from, to_, sort_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int _from: page start index
        :param int to: page end index
        :param choice sort_by: sort by a specific field
        :param bool desc: order of result

        :return: None
        :rtype: None
        """
        self.conds = conds
        self._from = _from
        self.to_ = to_
        self.sort_by = sort_by
        self.desc = desc
