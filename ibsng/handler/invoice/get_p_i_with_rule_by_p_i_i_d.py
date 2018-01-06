"""based on branch C_invoice info API method."""
from ibsng.handler.handler import Handler


class getPIWithRuleByPIID(Handler):
    """based on branch C_invoice info method class."""

    def setup(self, pi_id):
        """Setup required parameters.

        :param int pi_id: 
    
        :return: void
        :rtype: void
        """
        self.pi_id = pi_id
