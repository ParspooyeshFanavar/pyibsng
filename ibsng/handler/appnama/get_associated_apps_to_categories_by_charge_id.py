from ibsng.handler.handler import Handler


class getAssociatedAppsToCategoriesByChargeId(Handler):
    """Get all categories with their apps by charge id method."""

    def setup(self, charge_id):
        """Setup required parameters.

        :param int charge_id: charge id

        :return: None
        :rtype: None
        """
        self.charge_id = charge_id
