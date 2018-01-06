"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class searchProformaInvoices(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, conds, _from, to_, sort_by, desc):
        """Setup required parameters.

        :param dict conds: 
        :param int _from: pagination start
        :param int to: pagination end
        :param choice sort_by: 
        :param bool desc: descending
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self._from = _from
        self.to_ = to_
        self.sort_by = sort_by
        self.desc = desc
