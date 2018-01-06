"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class addInvoiceProfile(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, profile_name, isp_name=None, comment):
        """Setup required parameters.

        :param str profile_name: 
        :param str isp_name: 
        :param str comment: 
    
        :return: void
        :rtype: void
        """
        self.profile_name = profile_name
        self.isp_name = isp_name
        self.comment = comment
