""" info API method."""
from ibsng.handler.handler import Handler


class saveSearchExpiredUsers(Handler):
    """ info method class."""

    def setup(self, output_type, conds, order_by, desc, basic, attrs):
        """Setup required parameters.

        :param choice output_type: 
        :param dict conds: the same as searchExpiredUsers, at least one condition is necessary
        :param choice order_by: 
        :param bool desc: descending
        :param list basic: the same as user.saveSearchUser
        :param list attrs: the same as user.saveSearchUser
    
        :return: void
        :rtype: void
        """
        self.output_type = output_type
        self.conds = conds
        self.order_by = order_by
        self.desc = desc
        self.basic = basic
        self.attrs = attrs
