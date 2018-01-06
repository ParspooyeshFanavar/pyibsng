"""Get charge apps by charge id API method."""
from ibsng.handler.handler import Handler


class getAppsByChargeId(Handler):
    """Get charge apps by charge id method."""

    def setup(self, charge_id):
        """Setup required parameters.

        :param int charge_id: charge id

        :return: None
        :rtype: None
        """
        self.charge_id = charge_id
