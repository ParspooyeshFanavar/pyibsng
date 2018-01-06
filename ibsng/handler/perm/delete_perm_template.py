"""Admin Permission info API method."""
from ibsng.handler.handler import Handler


class deletePermTemplate(Handler):
    """Admin Permission info method class."""

    def setup(self, perm_template_name):
        """Setup required parameters.

        :param str perm_template_name: 
    
        :return: void
        :rtype: void
        """
        self.perm_template_name = perm_template_name
