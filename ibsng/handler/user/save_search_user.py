""" info API method."""
from ibsng.handler.handler import Handler


class saveSearchUser(Handler):
    """ info method class."""

    def setup(self, conds, order_by, desc, basic, attrs, output_type):
        """Setup required parameters.

        :param dict conds: the same as user.searchUser method
        :param choice order_by: 
        :param bool desc: 
        :param list basic: 
        :param list attrs: 
        :param choice output_type: 
    
        :return: void
        :rtype: void
        """
        self.conds = conds
        self.order_by = order_by
        self.desc = desc
        self.basic = basic
        self.attrs = attrs
        self.output_type = output_type
