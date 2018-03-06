"""Get associated apps to categories by charge ID API method."""
from ibsng.handler.handler import Handler


class getAssociatedAppsToCategoriesByChargeId(Handler):
    """Get all categories with their apps by charge ID class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.charge_id, int)

    def setup(self, charge_id):
        """Setup required parameters.

        :param int charge_id: charge id

        :return: None
        :rtype: None
        """
        self.charge_id = charge_id
