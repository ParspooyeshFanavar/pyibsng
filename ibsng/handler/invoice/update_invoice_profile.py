"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class updateInvoiceProfile(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, profile_id, profile_name, isp_name, comment, rules):
        """Setup required parameters.

        :param int profile_id: 
        :param str profile_name: 
        :param str isp_name: 
        :param str comment: 
        :param list rules: 
    
        :return: void
        :rtype: void
        """
        self.profile_id = profile_id
        self.profile_name = profile_name
        self.isp_name = isp_name
        self.comment = comment
        self.rules = rules
