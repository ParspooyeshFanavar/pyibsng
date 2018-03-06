"""Search for OTPs API method."""
from ibsng.handler.handler import Handler


class searchOTPs(Handler):
    """Search for OTPs class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.from_, int)
        self.is_valid(self.to_, int)
        self.is_valid(self.sort_by, str)
        self.is_valid(self.desc, bool)

    def setup(self, conds, from_, to_, sort_by, desc):
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
        self.from_ = from_
        self.to_ = to_
        self.sort_by = sort_by
        self.desc = desc
