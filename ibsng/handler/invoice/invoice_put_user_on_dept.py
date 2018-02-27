"""Invoice put user on dept API method."""
from ibsng.handler.handler import Handler


class invoicePutUserOnDept(Handler):
    """Invoice put user on dept method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.pi_id_list, list)

    def setup(self, pi_id_list):
        """Setup required parameters.

        :param list pi_id_list: list of proforma invoice ids

        :return: None
        :rtype: None
        """
        self.pi_id_list = pi_id_list
